# -*- coding: utf-8 -*-

from dataclasses import dataclass

from Models.staff.mixer import mixer
from appareilDAO import appareil


@dataclass
class mixerDao(appareil[]):

    def fond(self, fondeur: mixer):
        return 0

    def melange(self, fondeur: mixer):
        return 0

    def turbinage(self, fondeur: mixer):
        return 0