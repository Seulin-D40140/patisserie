# -*- coding: utf-8 -*-

from dataclasses import dataclass

from Models.staff.Fondeur import fondeur
from appareilDAO import appareil



@dataclass
class fonderDao(appareil[fondeur]):

    def fond(self, fonder : fondeur):
        nb_tours = mixer.chocolat * 6
        for no_tour in range(1, nb_tours + 1):
            print(f"\tJe fond {fonder.chocolat} g de chocolat, tour n°{no_tour}")
            time.sleep(0.5)


    def melange(self, mixeur : fondeur):
        return 0

    def turbinage(self, mixeur : fondeur):
        return 0

