#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ..ex3 import Creature

class BattleStrategy(ABC):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def is_valid(self) -> bool:
        ...

    @abstractmethod
    def act(self) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def __init__(self) -> None:
        self.creature = Creature()

    def is_valid(self) -> bool:
        return True

    def act(self) -> None:
        if self.is_valid() == True:
            return print(f"{}")