# ************************************************************************** #
#                                                                            #
#                                                         :::      ::::::::  #
#    capacitor.py                                          :+:      :+:    :+:  #
#                                                     +:+ +:+         +:+    #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+       #
#                                                 +#+#+#+#+#+   +#+          #
#    Created: 2026/09/24 20:29:28 by azahino-          #+#    #+#            #
#    Updated: 2026/09/24 20:29:29 by azahino-         ###   ########.fr      #
#                                                                            #
# ************************************************************************** #

from ex1 import factorys as f


def creation(fac: f.CreatureFactory) -> f.C.Creature:
    base = fac.create_base()
    evolved = fac.create_evolved()

    print(
        f"{base.describe()}\n"
        f"{base.attack()}"
    )
    print(
        f"{evolved.describe()}\n"
        f"{evolved.attack()}" 
    )


def battle(mons_1: f.CreatureFactory, mons_2: f.CreatureFactory) -> None:
    base_1 = mons_1.create_base()
    base_2 = mons_2.create_base()

    print(
        f"{base_1.describe()}\n"
        " vs.\n"
        f"{base_2.describe()}"
        " fight!"
        f"{base_1.attack()}\n"
        f"{base_2.attack()}"
    )

print("Testing Creature with healing capability")
creation(f.HealingCreatureFactory())

print("\nTesting Creature with transform capability")
creation(f.TransformCreatureFactory())
