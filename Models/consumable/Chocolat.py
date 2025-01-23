# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
from Ingredients import ingredients


@dataclass
class chocolat(ingredients):

    nombre : int

    def __str__(self) -> str:
        ingredient_str = super().__str__()
        return f"{ingredient_str} , {self.nombre} grammes"
