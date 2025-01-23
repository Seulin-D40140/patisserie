# -*- coding: utf-8 -*-

from dataclasses import dataclass
from Models.consumable.Ingredients import ingredients


@dataclass
class recipient():

    name : str

    def __str__(self) -> str:
        return f"name : {self.name}"