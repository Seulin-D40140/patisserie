# -*- coding: utf-8 -*-

from dataclasses import dataclass
from typing import Optional

from Models.staff.mixer import mixer
from Models.staff.melangeur import mixeur
from appareilDAO import appareil



@dataclass
class cuissonDao(appareil[mixeur]):

    def fond(self, mixeur : mixer):
        return 0

    def melange(self, mixeur : mixer):
        return 0

    def turbinage(self, mixeur : mixer):
        return 0

