import os
from os import environ
from pathlib import Path
from typing import (
    Any,
    Callable,
    Iterator,
    MutableMapping,
    TypeVar,
    Union,
    overload,
)

from gyver.attrs import define, info

from config._helpers import clean_dotenv_value, lazyfield, panic
from config.exceptions import InvalidCast, InvalidEnv, MissingName
from config.interface import MISSING, _default_cast

T = TypeVar("T")


@define
class EnvMapping(MutableMapping[str, str]):
    mapping: MutableMapping[str, str] = environ
    already_read: set[str] = info(default_factory=set)

    def __getitem__(self, name: str):
        val = self.mapping[name]
        self.already_read.add(name)
        return val

    def __setitem__(self, name: str, value: str):
        if name in self.already_read:
            raise panic(
                KeyError, f"{name} already read, cannot change its value"
            )
        self.mapping[name] = value

    def __delitem__(self, name: str) -> None:
        if name in self.already_read:
            raise panic(KeyError, f"{name} already read, cannot delete")
        del self.mapping[name]

    def __iter__(self) -> Iterator[str]:
        yield from self.mapping

    def __len__(self) -> int:
        return len(self.mapping)


default_mapping = EnvMapping()


@define
class Config:
    env_file: Union[str, Path, None] = None
    mapping: EnvMapping = default_mapping

    def __post_init__(self):
        if self.env_file and os.path.isfile(self.env_file):
            self.file_values.update(dict(self._read_file(self.env_file)))

    @lazyfield
    def file_values(self):
        return {}

    def _read_file(self, env_file: Union[str, Path]):
        with open(env_file, "r") as buf:
            for line in buf:
                line = (
                    line.strip()
                )  # Remove leading/trailing whitespaces and newlines
                if not line or line.startswith(
                    "#"
                ):  # Skip empty lines and full-line comments
                    continue

                # Handle lines with comments after the value

                name, value = line.split("=", 1)
                if " #" in value:
                    value, comment = value.strip().split(" #", 1)
                    maybe_quote = value[0]
                    if (
                        maybe_quote in "'\""
                        and value[-1] != maybe_quote
                        and comment[-1] == maybe_quote
                    ):
                        value = f"{value} #{comment}"

                yield name.strip(), clean_dotenv_value(value)

    def _cast(self, name: str, val: Any, cast: Callable) -> Any:
        try:
            val = cast(val)
        except Exception as e:
            raise panic(
                InvalidCast, f"{name} received an invalid value {val}"
            ) from e
        else:
            return val

    def _get_val(
        self, name: str, default: Union[Any, type[MISSING]] = MISSING
    ) -> Union[Any, type[MISSING]]:
        return self.mapping.get(name, self.file_values.get(name, default))

    def get(
        self,
        name: str,
        cast: Callable = _default_cast,
        default: Union[Any, type[MISSING]] = MISSING,
    ) -> Any:
        val = self._get_val(name, default)
        if val is MISSING:
            raise panic(
                MissingName, f"{name} not found and no default was given"
            )
        return self._cast(name, val, cast)

    @overload
    def __call__(
        self,
        name: str,
        cast: Union[Callable[[Any], T], type[T]] = _default_cast,
        default: type[MISSING] = MISSING,
    ) -> T:
        ...

    @overload
    def __call__(
        self,
        name: str,
        cast: Union[Callable[[Any], T], type[T]] = _default_cast,
        default: T = ...,
    ) -> T:
        ...

    def __call__(
        self,
        name: str,
        cast: Union[Callable[[Any], T], type[T]] = _default_cast,
        default: Union[T, type[MISSING]] = MISSING,
    ) -> T:
        return self.get(name, cast, default)
