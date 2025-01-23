import dataclasses

from DAO.mixerDAO import mixerDao
from DAO.fonderDAO import fonderDao
from Models.staff.Fondeur import fondeur
from Models.staff.Melangeur import melangeur


@dataclasses
class kitchen:

    @staticmethod
    def work_mix_ingredients(mixer : melangeur):
        mix : mixerDao = mixerDao()
        return mixerDao(mixer)

    @staticmethod
    def work_fond_chocolat(fonder: fondeur):
        mix: fonderDAO = fonderDAO()
        return fonderDAO(fonder)