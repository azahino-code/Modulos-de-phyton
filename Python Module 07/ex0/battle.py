# ************************************************************************** #
#                                                                            #
#                                                         :::      ::::::::  #
#    battle.py                                          :+:      :+:    :+:  #
#                                                     +:+ +:+         +:+    #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+       #
#                                                 +#+#+#+#+#+   +#+          #
#    Created: 2026/09/24 20:29:28 by azahino-          #+#    #+#            #
#    Updated: 2026/09/24 20:29:29 by azahino-         ###   ########.fr      #
#                                                                            #
# ************************************************************************** #

from ex0 import factorys as f


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


def battle(monster_1: f.FlameFactory, monster_2: f.WaterFactory) -> None:
    base_1 = monster_1.create_base()
    base_2 = monster_2.create_base()

    print(
        f"{base_1.describe()}\n"
        " vs.\n"
        f"{base_2.describe()}"
        " fight!"
        f"{base_1.attack()}\n"
        f"{base_2.attack()}"
    )

print("Testing factory")
creation(f.FlameFactory())

print("\nTesting factory")
creation(f.WaterFactory())

print("\nTesting battle")
battle(f.FlameFactory(), f.WaterFactory())
