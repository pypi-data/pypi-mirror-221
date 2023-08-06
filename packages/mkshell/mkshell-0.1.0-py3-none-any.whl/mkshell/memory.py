from tinydb import TinyDB, where, Query
from pathlib import Path
from addict import Addict

from typing import Any, Self, Union

__all__ = ["Pkg", "Memory"]

dbDefaultCache = {
    "commands": [],
    "tables": [],
    "flags" : {},
    "args": {}
}

Pkg = Path(__file__).parent
dbPath = Pkg / '.cache.json'


class Memory:
    @classmethod
    def __new__(cls, db: TinyDB = None, cache: Union[str, Path] = dbPath ):
        cls.path = cache
        cls.tinydb = db or TinyDB(cls.path)
        cls.tables = {}
        
    @classmethod
    def reset(cls):
        cls.tinydb.truncate()
        
    @classmethod
    def count(cls):
        return cls.tinydb.count()
    
    @classmethod
    def table(cls, name: str):
        t = cls.tinydb.table(name=name)
        cls.tables.update({
            name: t
        })
        m = Memory(t)
        setattr(cls, name, m)
        return m
    
    @classmethod
    def get(cls, key:str) -> str:
        return Addict(cls.db.get(where("key") == key))
    
    @classmethod
    def set(cls, key:str, value: Any) -> None:
        cls.tinydb.upsert({
            "key":key,
            "value":value
            },
            where("key") == key
        )
        
    @classmethod
    def add(cls, name: str) -> Self:
        return cls.table(name)
    
defaultMemory = Memory()
"""The default store for the app"""