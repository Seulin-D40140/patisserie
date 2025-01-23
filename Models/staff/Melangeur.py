# -*- coding: utf-8 -*-

from dataclasses import dataclass
from Models.staff.commis import commis
from Models.consumable.Oeuf import  eggs
from Models.consumable.Chocolat import chocolat
from Models.recipients.Recipient import recipient


@dataclass
class melangeur(commis):
    name: str
    recipient : recipient
    time : int

    def __str__(self) -> str:
        commis_str = super().__str__()
        return f"{commis_str} - nom : {self.name} - recipent : {self.recipient} - oeufs : {self.time}"