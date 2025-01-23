# -*- coding: utf-8 -*-

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class appareil[T](ABC):

    @abstractmethod
    def fond(self, obj: T):
        ...

    @abstractmethod
    def melange(self, obj: T):
        ...

    @abstractmethod
    def turbinage(self, obj: T):
        ...

