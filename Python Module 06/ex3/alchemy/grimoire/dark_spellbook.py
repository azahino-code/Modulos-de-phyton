# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    light_spellbook.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/23 21:41:37 by azahino-          #+#    #+#             #
#    Updated: 2026/09/23 21:41:37 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .dark_validator import validate_ingredients

def dark_spell_allowed_ingredients() -> list[str]:
    allowed_ingredients: list[str] = [
        "bats",
        "frogs",
        "arsenic",
        "eyeball"
    ]
    return allowed_ingredients

def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "VALID" in result:
        print(
            "Testing record dark spell: Spell recorded: "
            f"{spell_name} ({result})"
        )
    else:
        print(
            "Testing record dark spell: Spell rejected: "
            f"{spell_name} ({result})"
        )
