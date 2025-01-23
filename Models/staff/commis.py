# -*- coding: utf-8 -*-


from dataclasses import dataclass
from abc import ABC


@dataclass
class commis(ABC):
    name : str
    fonction : str

    def __str__(self) -> str:
        return f"nom : {self.name} , fonction : {self.fonction}"