# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    creatures.py                                       :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/24 20:31:13 by azahino-          #+#    #+#             #
#    Updated: 2026/09/24 20:31:14 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self) -> None:
        ...

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> None:
        return f"{self.name} is {self.type} type Creature"


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Flameling"
        self.type = "Fire"
        self.move = "Ember"

    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Pyrodon"
        self.type = "Fire/Fliying"
        self.move = "Flamethrower"

    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"

class Aquahub(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Aquahub"
        self.type = "Water"
        self.move = "Water Gun"

    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"

class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Torragon"
        self.type = "Water"
        self.move = "Hydro Pump"

    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"
