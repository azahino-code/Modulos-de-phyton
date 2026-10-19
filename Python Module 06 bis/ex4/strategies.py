#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex3 import Creature, TransformCapability, TransformationFactory

class BattleStrategy(ABC):
    def __init__(self, creature) -> None:
        self.creature = creature

    @abstractmethod
    def is_valid(self) -> bool:
        ...

    @abstractmethod
    def act(self) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def __init__(self, creature: Creature) -> None:
        super().__init__(creature)

    def is_valid(self) -> bool:
        if isinstance(self.creature, Creature):
            return True
        else:
            return False

    def act(self) -> None:
        try:
            if self.is_valid() == True:
                print(f"{self.creature.attack()}")
            else:
                raise Exception(
                    f"Invalid Creature '{self.creature.name}'"
                    "for this normal strategy"
                )
        except Exception as error:
            print(f"Battle error, aborting tournament: {error}")

class AggressiveStrategy(BattleStrategy):
    def __init__(self, creature: Creature):
        super().__init__(creature)

    def is_valid(self) -> bool:
        if isinstance(self.creature, TransformCapability):
            return True
        else:
            return False

    def act(self) -> None:
        try:
            if self.is_valid() == True:
                print(
                    f"{self.creature.transform()}\n"
                    f"{self.creature.attack()}\n"
                    f"{self.creature.revert()}"
                )
            else:
                raise Exception(
                    f"Invalid Creature '{self.creature.name}'"
                    "for this aggressive strategy"
                )
        except Exception as error:
            print(f"Battle error, aborting tournament: {error}")