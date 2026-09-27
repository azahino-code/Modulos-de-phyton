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

import capacitor
# Tipo Fuego

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

# Tipo Agua

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

# Tipo Planta

class Sproutling(Creature, capacitor.HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Sproutling"
        self.type = "Grass"
        self.move = "Vine whip"
        self.evolved = False

    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"

class Bloomelle(Creature, capacitor.HealCapability):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Bloomelle"
        self.type = "Grass/Fairy"
        self.move = "Petal Dance"
        self.evolved = True

    def attack(self) -> str:
        return f"{self.name} uses {self.move}!"

#Tipo Normal

class Shiftling(Creature, capacitor.TransformCapability):
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

class Morphagon(Creature, capacitor.TransformCapability):
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
        return f"{self.name} shifts into a dragonic battle form!"

    def revert(self) -> str:
        self.shifted = False
        return f"{self.name} stablizes its form."