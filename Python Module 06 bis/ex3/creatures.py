from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> None:
        return f"{self.name} is {self.type} type Creature"

from .habilities import TransformCapability

# Primera parte (Clases de Fuego)
class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire/Fliying"

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"

# 2 Parte. Clases con habilidades
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Shiftling"
        self.type = "Normal"
        self.shifted = False

    def attack(self) -> str:
        if self.shifted == False:
            return f"{self.name} attacks normally."
        else:
            return f"{self.name} performs a boosted strike!"

    def transform(self) -> str:
        self.shifted = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.shifted = False
        return f"{self.name} returns to normal."

class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Morphagon"
        self.type = "Normal/Dragon"
        self.shifted = False

    def attack(self) -> str:
        if self.shifted == False:
            return f"{self.name} attacks normally"
        else:
            return f"{self.name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self.shifted = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.shifted = False
        return f"{self.name} stabilizes its form."

