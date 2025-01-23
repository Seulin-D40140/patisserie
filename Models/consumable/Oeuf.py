# -*- coding: utf-8 -*-

from dataclasses import dataclass
from Models.consumable.Ingredients import ingredients


@dataclass
class eggs(ingredients):

    def __str__(self) -> str:
        ingredient_str = super().__str__()
        return f"{ingredient_str}, - nombre : {self.nombre}"
