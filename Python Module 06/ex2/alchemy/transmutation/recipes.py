# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    recipes.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.co    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/22 19:06:12 by azahino-          #+#    #+#             #
#    Updated: 2026/09/22 19:06:13 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from alchemy import elements
from .. import potions as p

def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew"
        f"'{elements.create_air()}' and '{p.strength_potion()}'"
        f"mixed with '{elements.create_fire()}'"
    )
