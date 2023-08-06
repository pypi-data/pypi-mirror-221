from typing import Mapping, Type, TypeVar
from dataclasses import dataclass, asdict
from . import pd_data_store
from abc import ABC
import json


T = TypeVar("T", bound="BaseTable")


@dataclass
class BaseTable(ABC):
    def to_str(self) -> str:
        dict_repr = asdict(self)
        return json.dumps(dict_repr)

    @classmethod
    def from_str(cls: Type[T], raw: str) -> "BaseTable":
        dict_repr = json.loads(raw)
        return cls(**dict_repr)

    @classmethod
    def load(cls: Type[T], key: str, data_store: Mapping) -> "BaseTable":
        store_at = f"{cls.__name__}:{key}"
        str_repr = pd_data_store.load(data_store, store_at)
        return cls.from_str(str_repr)

    def store(self, key: str, data_store: Mapping):
        str_repr = self.to_str()
        load_from = f"{self.__class__.__name__}:{key}"
        pd_data_store.store(data_store, load_from, str_repr)
