import threading
import time
import math

from Models.consumable.Chocolat import chocolat
from Models.consumable.Oeuf import eggs
from Models.recipients.Recipient import recipient
from Models.staff.Fondeur import fondeur
from Models.staff.Batteur import batteur


class BatteurOeufs(threading.Thread):
    def __init__(self, nb_oeufs):
        threading.Thread.__init__(self)
        self.nb_oeufs = nb_oeufs

    def run(self):

        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\tJe bats les {self.nb_oeufs} oeufs, tour n°{no_tour}")
            time.sleep(0.5)


class FondeurChocolat(threading.Thread):
    def __init__(self, quantite):
        threading.Thread.__init__(self)
        self.quantite = quantite

    def run(self):
        print("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print("Je verse l'eau dans une casserole")
        time.sleep(2)
        print("J'y pose le bol rempli de chocolat")
        time.sleep(1)

        nb_tours = math.ceil(self.quantite / 10)
        for no_tour in range(1, nb_tours + 1):
            print(f"Je mélange {self.quantite} de chocolat à fondre, tour n°{no_tour}")
            time.sleep(1)


if __name__ == "__main__":
    cul_de_poule = recipient("cul de poule")
    chocolat = chocolat(200)
    fondeur1 = fondeur("Nel" , cul_de_poule , chocolat)

    batter = recipient("batter")
    oeufs = eggs(6)
    batteur1 = batteur("Angel" , batter , oeufs)


    print("\nJe peux à présent incorporer le chocolat aux oeufs")
