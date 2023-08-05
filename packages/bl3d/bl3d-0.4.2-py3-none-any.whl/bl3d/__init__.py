# bl3d --- Domain Driven Design library
# Copyright © 2022, 2023 Bioneland
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

import re
import warnings
from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from typing import Any, Optional, Type, TypeVar

import pkg_resources

__version__ = pkg_resources.get_distribution(__name__).version


TypeDateAndTime = TypeVar("TypeDateAndTime", bound="DateAndTime")
TypeDate = TypeVar("TypeDate", bound="Date")
TypeDuration = TypeVar("TypeDuration", bound="Duration")
TypeFloat = TypeVar("TypeFloat", bound="Float")
TypeInteger = TypeVar("TypeInteger", bound="Integer")
TypeString = TypeVar("TypeString", bound="String")


class InvalidValue(ValueError):
    def __init__(self, message: str) -> None:
        super().__init__(f"Invalid value: {message}.")


class StringTooShort(InvalidValue):
    def __init__(self, minimum: int) -> None:
        super().__init__(f"minimum length is {minimum}.")
        self.MIN = minimum


class StringTooLong(InvalidValue):
    def __init__(self, maximum: int) -> None:
        super().__init__(f"maximum length is {maximum}.")
        self.MAX = maximum


class NumberTooSmall(InvalidValue):
    def __init__(self, minimum: float) -> None:
        super().__init__(f"minimum value is {minimum}.")
        self.MIN = minimum


class NumberTooBig(InvalidValue):
    def __init__(self, maximum: float) -> None:
        super().__init__(f"maximum value is {maximum}.")
        self.MAX = maximum


class DateAndTimeWithoutTimezone(InvalidValue):
    def __init__(self) -> None:
        super().__init__("timezone must be defined.")


class DurationNegative(InvalidValue):
    def __init__(self) -> None:
        super().__init__("duration cannot be negative.")


@dataclass(frozen=True)
class ValueObject(ABC):
    """An object whose equality is not based on identity by on value.

    It **MUST** contains an `instanciate` method that validates
    business rules and return a valid value object.
    Unfortunatly, the signature of this method will depend on the
    value objet considered and cannot hard coded with a
    `@abstractmethod`.

    The business rules **SHOULD** not be verified when loading an object
    that was persisted and `__init__` should be used instead.
    """

    NAME = ""

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Two different value objects with the same values are considered equal."""
        ...


@dataclass(frozen=True)
class String(ValueObject):
    __value: str
    MIN: Optional[int] = None
    MAX: Optional[int] = None

    @classmethod
    def instanciate(cls: Type[TypeString], value: str) -> TypeString:
        if cls.MIN is not None and len(value) < cls.MIN:
            raise StringTooShort(cls.MIN)
        if cls.MAX is not None and len(value) > cls.MAX:
            raise StringTooLong(cls.MAX)
        return cls(value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, String):
            return NotImplemented

        return other.__value == self.__value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(value=`{self.__value}`, MIN=`{self.MIN}`, MAX=`{self.MAX}`)"
        )

    def __str__(self) -> str:
        return self.__value


@dataclass(frozen=True)
class Integer(ValueObject):
    __value: int
    MIN: Optional[int] = None
    MAX: Optional[int] = None

    @classmethod
    def instanciate(cls: Type[TypeInteger], value: int) -> TypeInteger:
        if cls.MIN is not None and value < cls.MIN:
            raise NumberTooSmall(cls.MIN)
        if cls.MAX is not None and value > cls.MAX:
            raise NumberTooBig(cls.MAX)
        return cls(value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Integer):
            return NotImplemented

        return other.__value == self.__value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(value=`{self.__value}`, MIN=`{self.MIN}`, MAX=`{self.MAX}`)"
        )

    def __str__(self) -> str:
        return str(self.__value)

    def __int__(self) -> int:
        return self.__value


@dataclass(frozen=True)
class Float(ValueObject):
    __value: float
    MIN: Optional[float] = None
    MAX: Optional[float] = None

    @classmethod
    def instanciate(cls: Type[TypeFloat], value: float) -> TypeFloat:
        if cls.MIN is not None and value < cls.MIN:
            raise NumberTooSmall(cls.MIN)
        if cls.MAX is not None and value > cls.MAX:
            raise NumberTooBig(cls.MAX)
        return cls(value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Float):
            return NotImplemented
        return other.__value == self.__value

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"(value=`{self.__value}`, MIN=`{self.MIN}`, MAX=`{self.MAX}`)"
        )

    def __str__(self) -> str:
        return str(self.__value)

    def __float__(self) -> float:
        return self.__value


@dataclass(frozen=True)
class Date(ValueObject):
    __value: date

    @classmethod
    def instanciate(cls: Type[TypeDate], value: date) -> TypeDate:
        return cls(value)

    @classmethod
    def from_isoformat(cls: Type[TypeDate], isoformat: str) -> TypeDate:
        return cls.instanciate(date.fromisoformat(isoformat))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return other.__value == self.__value

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return self.__value < other.__value

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return self.__value <= other.__value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return self.__value > other.__value

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Date):
            return NotImplemented
        return self.__value >= other.__value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={repr(self.__value)})"

    def to_date(self) -> date:
        return date(self.__value.year, self.__value.month, self.__value.day)

    def format(self, fmt: str) -> str:
        return self.__value.strftime(fmt)


@dataclass(frozen=True)
class DateAndTime(ValueObject):
    __value: datetime

    @classmethod
    def instanciate(cls: Type[TypeDateAndTime], value: datetime) -> TypeDateAndTime:
        if not value.tzinfo:
            raise DateAndTimeWithoutTimezone()
        return cls(value)

    @classmethod
    def from_isoformat(cls: Type[TypeDateAndTime], isoformat: str) -> TypeDateAndTime:
        dt = datetime.fromisoformat(isoformat)
        if not dt.tzinfo:
            raise DateAndTimeWithoutTimezone()
        return cls.instanciate(dt.astimezone(timezone.utc))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DateAndTime):
            return NotImplemented
        return other.__value == self.__value

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, DateAndTime):
            return NotImplemented
        return self.__value < other.__value

    def __le__(self, other: object) -> bool:
        if not isinstance(other, DateAndTime):
            return NotImplemented
        return self.__value <= other.__value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, DateAndTime):
            return NotImplemented
        return self.__value > other.__value

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, DateAndTime):
            return NotImplemented
        return self.__value >= other.__value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={repr(self.__value)})"

    def to_datetime(self) -> datetime:
        return self.__value.replace()

    def format(self, fmt: str) -> str:
        return self.__value.strftime(fmt)

    def to_isoformat(self) -> str:
        return self.__value.isoformat()


@dataclass(frozen=True)
class Duration(ValueObject):
    __value: timedelta

    @classmethod
    def instanciate(cls: Type[TypeDuration], value: timedelta) -> TypeDuration:
        if value.total_seconds() < 0:
            raise DurationNegative()
        return cls(value)

    @classmethod
    def hours(cls: Type[TypeDuration], value: float) -> TypeDuration:
        return cls.instanciate(timedelta(hours=value))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Duration):
            return NotImplemented

        return other.__value == self.__value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(value={repr(self.__value)}"

    def to_hours(self) -> float:
        return float(self.__value.total_seconds() / 60 / 60)


class Entity(ABC):
    """A domain concept with an identity.

    They have methods that implement business rules and behaviour.
    Those methods mutate the state of the entity and emit events
    reflecting the changes.

    In Python, there is no way to "emit" events, so they are returned
    by the methods. But they are not, so to speak, return values.
    """

    pass


@dataclass(frozen=True)
class DomainEvent(ABC):
    """An event that happened in the domain."""

    version: int

    @abstractproperty
    def aggregate_id(self) -> str:
        """An identifier that uniquely identifies the aggregate
        that emitted the domain event.
        """
        ...

    @property
    def entity_unique_identifier(self) -> str:
        """Deprecated. Use `aggregate_id` instead."""
        warnings.warn(
            "Deprecated. Use `aggregate_id` instead.", DeprecationWarning, stacklevel=2
        )
        return self.aggregate_id


@dataclass(frozen=True)
class EntityState(ABC):
    """The state of an entity.

    A new state is created by applying an domain event to it.
    """

    class UnknownEvent(Exception):
        pass

    class IncompatibleVersions(Exception):
        pass

    version: int

    def apply(self, event: DomainEvent) -> "EntityState":
        if self.version != event.version:
            raise EntityState.IncompatibleVersions(f"{self.version} vs {event.version}")

        event_name = event.__class__.__name__
        method_name = f"apply_{camel_to_snake(event_name)}"
        if method := getattr(self, method_name, None):
            return method(event)  # type: ignore
        raise EntityState.UnknownEvent(event_name)


class History(ABC):
    """A sequence of events that happened inside the domain."""

    class EvenNotHandled(NotImplementedError):
        def __init__(self, name: str) -> None:
            super().__init__(f"History cannot handle event `{name}`!")

    class ReadError(AttributeError):
        def __init__(self, name: str, data: dict[str, Any]) -> None:
            super().__init__(f"Cannot read event's data `{name}`: {data}")

    @abstractmethod
    def read(self, stream: str) -> list[DomainEvent]:
        ...

    @abstractmethod
    def __lshift__(self, domain_events: list[DomainEvent]) -> None:
        ...


def camel_to_snake(string: str) -> str:
    # https://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-snake-case
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", string)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()
