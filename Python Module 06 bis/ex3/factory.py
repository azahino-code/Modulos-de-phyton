from abc import ABC, abstractmethod
from . import creatures as C


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> C.Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> C.Creature:
        pass


class FireFactory(CreatureFactory):
    def create_base(self) -> C.Flameling:
        return C.Flameling("Flameling", "Fire")

    def create_evolved(self) -> C.Pyrodon:
        return C.Pyrodon("Pyrodon", "Fire/Flying")


class TransformationFactory(CreatureFactory):
    def create_base(self) -> C.Shiftling:
        return C.Shiftling("Shiftling", "Normal")

    def create_evolved(self) -> C.Morphagon:
        return C.Morphagon("Morphagon", "Normal/Dragon")
