# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
from abc import ABC


@dataclass
class ingredients(ABC):
    name : str
    quantity : int

    def __str__(self) -> str:
        return f"name : {self.name} - quantiter : {self.quantity}"