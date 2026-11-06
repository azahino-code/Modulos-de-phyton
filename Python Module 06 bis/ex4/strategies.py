#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex3.creatures import Creature
from ex3.habilities import TransformCapability


class InvalidStrategyError(Exception):
    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, creature: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(f"{creature.attack()}")
        else:
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}'"
                "for this normal strategy"
            )


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if self.is_valid(creature):
            print(
                f"{creature.transform()}\n"
                f"{creature.attack()}\n"
                f"{creature.revert()}"
            )
        else:
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' "
                "for this aggressive strategy"
            )
