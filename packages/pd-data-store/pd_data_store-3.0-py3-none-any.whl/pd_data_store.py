from typing import Mapping, Any
import json
import os


def _anonymize(data: str) -> str:
    if len(pwd := os.environ.get("DATA_STORE_PWD", "")) > 0:
        return "".join(chr(ord(c) ^ ord(p)) for c, p in zip(data, pwd * len(data)))
    else:
        raise RuntimeError("Database password not defined.")


def _de_anonymize(data: str) -> str:
    if len(pwd := os.environ.get("DATA_STORE_PWD", "")) > 0:
        return "".join(chr(ord(c) ^ ord(p)) for c, p in zip(data, pwd * len(data)))
    else:
        raise RuntimeError("Database password not defined.")


def store(data_store: Mapping, key: str, value: Mapping[Any, Any]):
    value_anonymized = _anonymize(json.dumps(value))
    key_anonymized = _anonymize(key)
    data_store[key_anonymized] = value_anonymized


def load(data_store: Mapping, key: str) -> Mapping[Any, Any]:
    value_anonymized = data_store[_anonymize(key)]
    return json.loads(_de_anonymize(value_anonymized))
