# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    light_validator.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/23 21:37:57 by azahino-          #+#    #+#             #
#    Updated: 2026/09/23 21:37:57 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .dark_spellbook import dark_spell_allowed_ingredients

def validate_ingredients(ingredients: str) -> str:
    for key in dark_spell_allowed_ingredients():
        if key in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
