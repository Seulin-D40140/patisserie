# -*- coding: utf-8 -*-

from dataclasses import dataclass

from Models.staff.commis import commis


@dataclass
class verseur(commis):

    name: str
    chocolat : int
    eggs : int

    def __str__(self) -> str:
        commis_str = super().__str__()
        return f"{commis_str} - nom : {self.name} - chocolat : {self.chocolat} - eggs : {self.eggs}"