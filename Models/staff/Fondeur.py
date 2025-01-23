# -*- coding: utf-8 -*-

from dataclasses import dataclass

from Models.recipients.Recipient import recipient
from Models.staff.commis import commis
from Models.consumable.Chocolat import chocolat


@dataclass
class fondeur(commis):

    name : str
    recipient : recipient
    chocolat : chocolat


    def __str__(self) -> str:
        commis_str = super().__str__()
        return f"{commis_str} - nom : {self.name} - ingredient : {self.chocolat} - recipient : {self.recipient}"