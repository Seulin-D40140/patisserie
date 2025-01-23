import threading
import time
import math

from Models.consumable.Chocolat import chocolat
from Models.consumable.Oeuf import eggs
from Models.recipients.Recipient import recipient
from Models.staff.Fondeur import fondeur
from Models.staff.Batteur import batteur
from Models.staff.Melangeur import melangeur
from Models.staff.Verseur import verseur


class Melangeur(threading.Thread):
    def __init__(self, mixer : melangeur):
        threading.Thread.__init__(self)
        self.nb_temps = mixer.time
        self.name = mixer.name

    def run(self):
        time.sleep(4)
        print(f"...... melangeur *- {self.name} -* je melange doucement ")

        nb_tours = self.nb_temps * 2
        for no_tour in range(1, nb_tours + 1):
            print(f"...... melangeur *- {self.name} -* Je je continue de melanger tour n°{no_tour}")
            time.sleep(1.2)

class Verseur(threading.Thread):
    def __init__(self, verser : verseur):
        threading.Thread.__init__(self)
        self.nb_chocolat = verser.chocolat
        self.nb_eggs = verser.eggs
        self.name = verser.name

    def run(self):
        if self.nb_eggs > 0:
            nb_tours = self.nb_eggs * 3
            name = "oeufs"
            print(f"---\t verseur .. {self.name} .. je recupere le recipient de  {name}")
            time.sleep(2)
        elif self.nb_chocolat > 0:
            nb_tours = math.ceil(self.nb_chocolat / 9)
            name ="chocolat"
            print(f"---\t verseur .. {self.name} .. je recupere le recipient de  {name}")
            time.sleep(2)
        for no_tour in range(1, nb_tours + 1):
            print(f"---\t verseur .. {self.name} .. Je verse {name} dans le recipient , tour n°{no_tour}")
            time.sleep(0.5)

class BatteurOeufs(threading.Thread):
    def __init__(self, batter : batteur):
        threading.Thread.__init__(self)
        self.nb_oeufs = batter.eggs.quantity
        self.name = batter.name

    def run(self):
        print(f"\tbatteur ~ {self.name} ~ je prepare le batteur ")
        time.sleep(3)
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\tbatteur ~ {self.name} ~ , Je bats les {self.nb_oeufs} oeufs, tour n°{no_tour}")
            time.sleep(0.5)
        print("******************** les oeufs sont pret a etre melanger **********************")


class FondeurChocolat(threading.Thread):
    def __init__(self, fonder : fondeur):
        threading.Thread.__init__(self)
        self.quantite = fonder.chocolat.quantity
        self.name = fonder.name

    def run(self):
        print(f"*** fondeur ++ {self.name} ++ Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print(f"*** fondeur ++ {self.name} ++ Je verse l'eau dans une casserole")
        time.sleep(2)
        print(f"*** fondeur ++ {self.name} ++ J'y pose le bol rempli de chocolat")
        time.sleep(0.8)

        nb_tours = math.ceil(self.quantite / 10)
        for no_tour in range(1, nb_tours + 1):
            print(f"*** fondeur ++ {self.name} ++ , Je mélange {self.quantite} de chocolat à fondre, tour n°{no_tour}")
            time.sleep(1)
        print("******************** le chocolat est pret a etre melanger **********************")
        time.sleep(2)




if __name__ == "__main__":
    cul_de_poule = recipient("cul de poule")
    chocolat = chocolat('chocolat' , 200)
    fondeur1 = fondeur("fondeur", "Nel" , cul_de_poule , chocolat)

    batter = recipient("batteur")
    oeufs = eggs("oeuf" , 6)
    batteur1 = batteur("batteur" , "Angel" , batter , oeufs)

    melangeur1 = melangeur('touilleur' , 'Arthur' , cul_de_poule, 10)

    verseur1 = verseur('verseur' , 'Gillou' , 0 , batteur1.eggs.quantity)
    verseur2 = verseur('verseur', 'Itai', fondeur1.chocolat.quantity, 0)


    b1 = BatteurOeufs(batteur1)
    b1.start()
    f1 = FondeurChocolat(fondeur1)
    f1.start()

    b1.join()
    f1.join()
    print("------------------------------\nJe peux à présent incorporer le chocolat aux oeufs")

    v1 = Verseur(verseur1)
    v1.start()
    v2 = Verseur(verseur2)
    v2.start()

    m1 = Melangeur(melangeur1)
    m1.start()

    v1.join()
    v2.join()
    m1.join()
    print("------------------------------\nJe peux à présent le mettre a cuir")
