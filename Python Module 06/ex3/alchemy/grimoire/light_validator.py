# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    light_validator.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.co    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/23 21:37:57 by azahino-          #+#    #+#             #
#    Updated: 2026/09/23 21:37:57 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from alchemy.grimoire.light_spellbook import light_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    for key in light_spell_allowed_ingredients():
        if key in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
