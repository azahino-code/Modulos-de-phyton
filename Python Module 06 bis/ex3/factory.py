from abc import ABC, abstractmethod
from . import creatures as C


class CreatureFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def create_base(self) -> C.Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> C.Creature:
        pass


class FireFactory(CreatureFactory):
    def __init__(self) -> None:
        super().__init__()

    def create_base(self) -> C.Creature:
        return C.Flameling()

    def create_evolved(self) -> C.Creature:
        return C.Pyrodon()


class TransformatioFactory(CreatureFactory):
    def __init__(self):
        super().__init__()

    def create_base(self):
        return C.Shiftling()

    def create_evolved(self) -> C.Creature:
        return C.Morphagon()
