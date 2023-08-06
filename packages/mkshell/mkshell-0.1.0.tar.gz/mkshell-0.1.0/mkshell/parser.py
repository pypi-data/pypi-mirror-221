import yaml

from .memory import defaultMemory
from typing import Self, Dict, Any
from addict import Addict

class Parser:
    @classmethod
    def __new__(cls, declaration: Dict[str, Any]) -> Self:
        cls.declaration = Addict(declaration)
        cls.memory = defaultMemory
        # check = cls.memory.db.get("all-commands")
        
    @classmethod
    def command(cls, name: str) -> Self:
        cls.declaration.commands