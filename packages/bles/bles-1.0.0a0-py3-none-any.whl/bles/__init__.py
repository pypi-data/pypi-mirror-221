# bles --- Event Sourcing library
# Copyright © 2021-2023 Bioneland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""
Classes required to implement event sourcing.

@see <https://barryosull.com/blog/projection-building-blocks-what-you-ll-need-to-build-projections/>  # noqa

## Life cycle


### Reading

- EVENT_STORE returns, for a given stream, an ordered list of
- EVENT [id, unique(stream, version), name, data, when]
- HISTORY converts (switch on `name`, pass `**data` to constructor) them to
- DOMAIN_EVENT
- REPOSITORY instanciate
- AGGREGATE
  * by passing domain events to the constructor;
  * only accepts domain events with `version` greater than its current version.


### Writing

- AGGREGATE emits a sequence (consecutive version numbers) of
- DOMAIN_EVENT written to
- HISTORY which converts them to
- EVENT which are persisted to
- EVENT_STORE if the events are coherent within a given stream
"""

import json
import logging
import sys
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from enum import Enum as Enumeration
from enum import auto
from importlib import metadata
from typing import Any, Iterator, Optional

import bl3d

__version__ = metadata.version(__package__ or __name__)


@dataclass(frozen=True)
class Event:
    """Something that happened."""

    stream_id: str
    version: int  # Must be unique in a given stream
    name: str
    data: dict[str, Any]
    position: int = 0
    recorded_at: Optional[datetime] = None

    @classmethod
    def from_string(cls, data: str) -> "Event":
        return cls.from_dict(json.loads(data))

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Event":
        recorded_at: Optional[datetime] = None
        if isoformat := data.get("recorded_at"):
            recorded_at = datetime.fromisoformat(isoformat)
            recorded_at = recorded_at.replace(tzinfo=timezone.utc)
        return cls(
            recorded_at=recorded_at,
            stream_id=data["stream_id"],
            version=data["version"],
            name=data["name"],
            data=data["data"],
            position=int(data.get("position", "0")),
        )

    def to_string(self) -> str:
        return json.dumps(
            dict(
                recorded_at=self.recorded_at.isoformat() if self.recorded_at else None,
                stream_id=self.stream_id,
                version=self.version,
                name=self.name,
                data=self.data,
                position=self.position,
            )
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class EventStore(ABC):
    """Repository for events."""

    @abstractmethod
    def record(self, events: list[Event]) -> None:
        ...

    @abstractmethod
    def for_stream(self, name: str) -> "EventStore":
        ...

    @abstractmethod
    def read(self, start: int = 0, follow: bool = False) -> Iterator[Event]:
        ...

    @abstractmethod
    def last_position(self) -> int:
        ...


class History(bl3d.History):
    EVENT_MODULE = sys.modules[__name__]

    class EvenNotHandled(NotImplementedError):
        def __init__(self, name: str) -> None:
            super().__init__(f"History cannot handle event `{name}`!")

    class ReadError(AttributeError):
        def __init__(self, name: str, data: dict[str, Any]) -> None:
            super().__init__(f"Cannot read event's data `{name}`: {data}")

    def __init__(self, event_store: EventStore) -> None:
        self.__store = event_store

    def read(self, stream: str) -> list[bl3d.DomainEvent]:
        return [self.__event(e) for e in self.__store.for_stream(stream).read()]

    def __event(self, event: Event) -> bl3d.DomainEvent:
        try:
            class_ = getattr(self.EVENT_MODULE, event.name)
            return class_(  # type: ignore
                **event.data,
                version=event.version,
            )
        except AttributeError:
            raise History.EvenNotHandled(event.name)
        except TypeError:
            raise History.ReadError(event.name, event.data)

    def __lshift__(self, domain_events: list[bl3d.DomainEvent]) -> None:
        self.__store.record(
            [
                Event(
                    stream_id=e.aggregate_id,
                    version=e.version,
                    name=e.__class__.__name__,
                    data=self.__event_as_dict(e),
                )
                for e in domain_events
            ]
        )

    def __event_as_dict(self, domain_event: bl3d.DomainEvent) -> dict[str, Any]:
        data = asdict(domain_event)
        del data["version"]
        return data


class ProjectorStatuses(Enumeration):
    # NEW
    # Never booted nor played. Never to be actually used.

    STALLED = auto()
    "Ready to be booted."

    OK = auto()
    "Successfully played."

    BROKEN = auto()
    "Crashed while being played."

    RETIRED = auto()
    "Never to be booted nor played again."


class Ledger(ABC):
    """Keeps track of a projector's lifecycle.

    From <https://barryosull.com/blog/managing-projectors-is-harder-than-you-think/>.
    """

    class UnknownProjector(Exception):
        def __init__(self, name: str) -> None:
            super().__init__(f"Unknown projector [name={name}]")

    class ProjectorAlreadyRegistered(Exception):
        def __init__(self, name: str) -> None:
            super().__init__(f"Projector already registered [name={name}]")

    @abstractmethod
    def status(self) -> tuple[str, ProjectorStatuses, int]:
        ...

    @abstractmethod
    def knows(self, name: str) -> bool:
        ...

    @abstractmethod
    def register(self, name: str) -> None:
        ...

    @abstractmethod
    def forget(self, name: str) -> None:
        ...

    @abstractmethod
    def position(self, name: str) -> int:
        ...

    @abstractmethod
    def update_position(self, name: str, position: int) -> None:
        ...

    @abstractmethod
    def find_broken(self) -> list[str]:
        ...

    @abstractmethod
    def find_stalled(self) -> list[str]:
        ...

    @abstractmethod
    def find_ok(self) -> list[str]:
        ...

    @abstractmethod
    def mark_as_stalled(self, name: str) -> None:
        ...

    @abstractmethod
    def mark_as_ok(self, name: str) -> None:
        ...

    @abstractmethod
    def mark_as_broken(self, name: str) -> None:
        ...

    @abstractmethod
    def mark_as_retired(self, name: str) -> None:
        ...


class ProjectorTypes(Enumeration):
    RUN_FROM_BEGINNING = auto()
    """Plays all the events during the boot phase then keep on playing new ones.

    Used, for instance, to populate a projection.
    """

    RUN_FROM_NOW = auto()
    """Skips the boot phase then play all the events as usual.

    Used, for instance, to send email notifications from now on.
    """

    RUN_ONCE = auto()
    """Plays existing events during the boot phase then does not play anymore.

    Used, for instance, to add new events to the store based on the old ones.
    """


class Projector(ABC):
    """Parses event's data and calls the proper projection method.

    Projectors exist in different types, that implement `boot` and `play` differently.
    """

    NAME: str
    TYPE: ProjectorTypes
    PREFIX: str = "when"

    class EventHandlerCrashed(Exception):
        def __init__(self, method_name: str, exception: Exception) -> None:
            super().__init__(
                "Event handler raised an exception! "
                f"[handler: {method_name}, "
                f"exception: {exception.__class__.__name__}, "
                f"message: {exception}]"
            )

    def process(self, event: Event) -> None:
        logger = logging.getLogger(f"Projector/{self.NAME}")

        method_name = f"{self.PREFIX}_{bl3d.camel_to_snake(event.name)}"
        method = getattr(self, method_name, None)
        if method:
            logger.info(
                f"Processing event. [projector={self.__class__.__name__}, "
                f"stream_id={event.stream_id}, version={event.version}, "
                f"name={event.name}]"
            )
            logger.debug(f"Data = {event.data}")
            try:
                method(event.data)
            except Exception as exc:
                raise Projector.EventHandlerCrashed(method_name, exc)
        else:
            logger.debug(f"No method to handle event. [name={event.name}]")


class Projection(ABC):
    """A "point of view" on the data.

    They contain methods to write data to the chosen storage
    (SQL, no-SQL, in-memory…) and methods to query the data back.
    """

    ...


class Projectionist:
    """Boots and runs all the registered projectors."""

    def __init__(self, store: EventStore, ledger: Ledger) -> None:
        self.__logger = logging.getLogger("Projectionist")
        self.__store = store
        self.__ledger = ledger
        self.__projectors: dict[str, Projector] = {}
        self.__last_seen_position: int = 0

    def register(self, projector: Projector) -> None:
        self.__projectors[projector.NAME] = projector

    def boot(self) -> None:
        self.__mark_new_projectors_as_stalled()
        self.__mark_broken_as_stalled()
        self.__boot_stalled_projectors()

    def __mark_new_projectors_as_stalled(self) -> None:
        for n, p in self.__projectors.items():
            if not self.__ledger.knows(n):
                self.__ledger.register(n)

    def __mark_broken_as_stalled(self) -> None:
        for name in self.__ledger.find_broken():
            self.__ledger.mark_as_stalled(name)

    def __boot_stalled_projectors(self) -> None:
        for name in self.__ledger.find_stalled():
            self.__boot_projector(name)

    def __boot_projector(self, name: str) -> None:
        try:
            current_position = self.__ledger.position(name) + 1
            projector = self.__projectors[name]
            for e in self.__store.read(start=current_position):
                if self.__is_bootable(projector):
                    projector.process(e)
                current_position = e.position
            if projector.TYPE == ProjectorTypes.RUN_ONCE:
                self.__ledger.mark_as_retired(name)
            else:
                self.__ledger.mark_as_ok(name)
            self.__ledger.update_position(name, current_position)
        except Exception as exc:
            self.__ledger.mark_as_broken(name)
            self.__logger.error(
                "Error while booting projector! "
                f"[projector={name}, error={exc.__class__.__name__}, "
                f"message={exc}]"
            )
            self.__logger.debug(exc)

    def __is_bootable(self, projector: Projector) -> bool:
        return projector.TYPE in [
            ProjectorTypes.RUN_FROM_BEGINNING,
            ProjectorTypes.RUN_ONCE,
        ]

    def play(self, follow: bool = False) -> None:
        list_projectors = self.__ledger.find_ok()
        positions = [self.__ledger.position(n) for n in list_projectors]
        current_position = min(positions) if positions else 0
        for e in self.__store.read(start=current_position + 1, follow=False):
            current_position = e.position
            for name in self.__ledger.find_ok():
                if e.position <= self.__ledger.position(name):
                    continue
                if (p := self.__projectors.get(name)) and self.__is_playable(p):
                    self.__process_event(p, e)

        if not follow:
            return

        for e in self.__store.read(start=current_position + 1, follow=True):
            for name in self.__ledger.find_ok():
                if (p := self.__projectors.get(name)) and self.__is_playable(p):
                    self.__process_event(p, e)

    def __process_event(self, projector: Projector, event: Event) -> None:
        try:
            projector.process(event)
            self.__ledger.update_position(projector.NAME, event.position)
        except Exception as exc:
            self.__ledger.mark_as_broken(projector.NAME)
            self.__logger.error(
                "Error while playing projector! "
                f"[projector={projector.NAME}, error={exc.__class__.__name__}, "
                f"message={exc}]"
            )

    def __is_playable(self, projector: Projector) -> bool:
        return projector.TYPE in [
            ProjectorTypes.RUN_FROM_BEGINNING,
            ProjectorTypes.RUN_FROM_NOW,
        ]
