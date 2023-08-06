import os
from dataclasses import field
from datetime import datetime
from typing import Any, Dict

from rispack.dynamodb.table import BaseDocument, Index, Table
from rispack.schemas import dataclass

CACHE_PREFIX = "CACHE#"


@dataclass
class CacheDocument(BaseDocument):
    cache_key: str
    cache_state: str
    expires_at: datetime = field(default=None)
    data: Dict[str, Any] = field(default=None)

    @classmethod
    def primary_key(cls):
        return Index(partition_key="{{cache_key}}", sort_key="{{cache_state}}")


class GlobalCache:
    @classmethod
    def instance(cls):
        cache_table = os.environ["CACHE_TABLE"]
        table = Table(
            name=cache_table,
            primary_key=Index(partition_key="PK", sort_key="SK"),
            documents=[CacheDocument],
        )

        return cls(table)

    def __init__(self, table):
        self.table = table
        self.connection = table.get_connection()

    def get(
        self, cache_key: str, cache_state: str = "CURRENT", data: Dict[str, Any] = None
    ):
        data = data or {}
        cache_key = CACHE_PREFIX + cache_key.format(**data)

        return self.connection.get(
            CacheDocument, key={"cache_key": cache_key, "cache_state": cache_state}
        )

    def invalidate(self, cache_key, cache_state="CURRENT"):
        db_key = CACHE_PREFIX + cache_key

        return self.connection.delete(
            CacheDocument, key={"cache_key": db_key, "cache_state": cache_state}
        )

    def set(self, cache_key: str, data: Dict[str, Any]):
        cache_key = cache_key.format(**data)
        db_key = CACHE_PREFIX + cache_key

        current = self.get(cache_key)

        if current:
            self.invalidate(cache_key)

        payload = {
            "cache_key": db_key,
            "cache_state": "CURRENT",
            "data": data,
        }

        item = CacheDocument.load(payload)

        self.connection.put(item)
        self.connection.commit()

        return item
