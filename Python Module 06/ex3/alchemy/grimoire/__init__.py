# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    __init__.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.co    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/23 22:26:25 by azahino-          #+#    #+#             #
#    Updated: 2026/09/23 22:26:25 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .light_spellbook import light_spell_record

from .dark_spellbook import dark_spell_record

all = [
    light_spell_record,
    dark_spell_record
]