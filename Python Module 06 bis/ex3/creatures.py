from abc import ABC, abstractmethod
from .habilities import TransformCapability


class Creature(ABC):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is {self._type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Flameling"
        self._type = "Fire"

    def attack(self) -> str:
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Pyrodon"
        self._type = "Fire/Flying"

    def attack(self) -> str:
        return f"{self._name} uses Flamethrower!"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Shiftling"
        self._type = "Normal"
        self._shifted: bool = False

    def attack(self) -> str:
        if not self._shifted:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} performs a boosted strike!"

    def transform(self) -> str:
        self._shifted = True
        return f"{self._name} shifts into a sharper form!"

    def revert(self) -> str:
        self._shifted = False
        return f"{self._name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__()
        self._name = "Morphagon"
        self._type = "Normal/Dragon"
        self._shifted = False

    def attack(self) -> str:
        if not self._shifted:
            return f"{self._name} attacks normally."
        else:
            return f"{self._name} unleashes a devastating morph strike!"

    def transform(self) -> str:
        self._shifted = True
        return f"{self._name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._shifted = False
        return f"{self._name} stabilizes its form."
