# -*- coding: utf-8 -*-


from dataclasses import dataclass, field
from typing import Optional
from abc import ABC


@dataclass
class ingredients(ABC):
    name : str
    quantity : int
    unity : str

    def __str__(self) -> str:
        return f"name : {self.name} - quantiter : {self.quantity} - uniter : {self.unity}"