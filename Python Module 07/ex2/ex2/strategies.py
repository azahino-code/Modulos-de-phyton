# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    strategies.py                                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/10/03 23:20:30 by azahino-          #+#    #+#             #
#    Updated: 2026/10/03 23:20:31 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
import creatures as c
import habilities as h


class BattleStrategy(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def is_valid(self) -> bool:
        ...
    
    @abstractmethod
    def act(self) -> str:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self)  -> bool:
        return True

    def act(self) -> str:
        if self.is_valid() == True:
            return c.Creature.attack()
        else:
            raise Exception(
                "Battle error, aborting tournament:"
                f" Invalid Creature {self.name} for this aggressive strategy"
            )


class AggressiveStrategy(BattleStrategy):
    def is_valid(self)  -> bool:
        if self == c.Creature and h.TransformCapability:
            return True
        else:
            return False

    def act(self) -> str:
        if self.is_valid() == True:
            return (
                c.Creature
            )
        else:
            raise Exception(
                "Battle error, aborting tournament:"
                f" Invalid Creature {self.name} for this aggressive strategy"
            )

class DefensiveStrategy(BattleStrategy):
    def is_valid(self)  -> bool:
        if self == c.Creature and h.HealCapability:
            return True
        else:
            return False

    def act(self) -> str:
        if self.is_valid() == True:
            return ""
        else:
            raise Exception(
                "Battle error, aborting tournament:"
                f" Invalid Creature {self.name} for this aggressive strategy"
            )