# -*- coding: utf-8 -*-


from dataclasses import dataclass
from abc import ABC


@dataclass
class commis(ABC):
    fonction : str

    def __str__(self) -> str:
        return f"fonction : {self.fonction}"