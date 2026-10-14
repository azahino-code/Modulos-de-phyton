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
        f"{base.attack()}\"
        f"{base.heal()}"
    )
    print(
        f"{evolved.describe()}\n"
        f"{evolved.attack()}" 
    )


print("Testing Creature with healing capability")
creation(f.HealingCreatureFactory())

print("\nTesting Creature with transform capability")
creation(f.TransformCreatureFactory())
