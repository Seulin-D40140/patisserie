# -*- coding: utf-8 -*-

from dataclasses import dataclass

from Models.staff.Melangeur import melangeur
from appareilDAO import appareil


@dataclass
class mixerDao(appareil[melangeur]):

    def fond(self, mixer: melangeur):
        return 0

    def melange(self, mixer: melangeur):
        nb_tours = mixer.chocolat * 8
        nb_tour2 = mixer.eggs *4
        for no_tour in range(1, nb_tours + 1):
            for tourEggs in range(1, nb_tours + 1):
                print(f"\tJe melange {melangeur.chocolat} g de chocolat et les oeuf, tour n°{no_tour}")
                time.sleep(0.5)

        return 0

    def turbinage(self, mixer: melangeur):
        return 0