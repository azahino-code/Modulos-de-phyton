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

def light_spell_allowed_ingredients() -> list[str]:
    allowed_ingredients: list[str] = [
        "earth",
        "fire",
        "water",
        "air"
    ]
    return allowed_ingredients

from alchemy.grimoire.light_validator import validate_ingredients

def light_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return(
            "Testing record light spell: Spell recorded: "
            f"{spell_name} ({result})"
        )
    else:
        return(
            "Testing record light spell: Spell rejected: "
            f"{spell_name} ({result})"
        )
