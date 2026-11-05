#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex3.creatures import Creature, TransformCapability


class InvalidStrategyError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class BattleStrategy(ABC):
    def __init__(self, creature: Creature) -> None:
        self.c_reature = creature

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
        return isinstance(self.creature, Creature)

    def act(self) -> None:
        if self.is_valid():
            print(f"{self.creature.attack()}")
        else:
            raise InvalidStrategyError(
                f"Invalid Creature '{self.creature.name}'"
                "for this normal strategy"
            )

class AggressiveStrategy(BattleStrategy):
    def __init__(self, creature: Creature):
        super().__init__(creature)

    def is_valid(self) -> bool:
        return isinstance(self._creature, TransformCapability)

    def act(self) -> None:
        if self.is_valid():
            print(
                f"{self.creature.transform()}\n"
                f"{self.creature.attack()}\n"
                f"{self.creature.revert()}"
            )
        else:
            raise InvalidStrategyError(
                f"Invalid Creature '{self._creature._name}'"
                "for this aggressive strategy"
            )
