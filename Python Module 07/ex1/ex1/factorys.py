# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    factorys.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/25 18:32:36 by azahino-          #+#    #+#             #
#    Updated: 2026/09/25 18:34:58 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

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

    def create_base(self) -> C.Creature:
        return C.Aquahub()

    def create_evolved(self) -> C.Creature:
        return C.Torragon()

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> C.Creature:
        return C.Sproutling()

    def create_evolved(self) -> C.Creature:
        return C.Bloomelle()

class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> C.Creature:
        return C.Shiftling()

    def create_evolved(self) -> C.Creature:
        return C.Morphagon()
