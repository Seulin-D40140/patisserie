# -*- coding: utf-8 -*-

from dataclasses import dataclass

from Models.consumable.Chocolat import chocolat
from Models.recipients.Recipient import recipient
from Models.staff.commis import commis
from Models.consumable.Oeuf import eggs


@dataclass
class batteur(commis):

    name: str
    recipient : recipient
    eggs : eggs

    def __str__(self) -> str:
        commis_str = super().__str__()
        return f"{commis_str} - nom : {self.name} - coeuf : {self.eggs}"