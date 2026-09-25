# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    potions.py                                         :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/22 17:58:53 by azahino-          #+#    #+#             #
#    Updated: 2026/09/22 17:58:54 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import alchemy.elements

elements = alchemy.elements


def healing_potion() -> str:
    return (
        "Healing potion brewed with "
        f"'{elements.create_earth()}' and '{elements.create_air()}'"
    )


def strength_potion() -> str:
    return (
        "Strength potion brewed with "
        f"'{elements.create_fire()}' and '{elements.create_water()}'"
    )
