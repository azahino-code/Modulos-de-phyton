# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_kaboom_0.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.co    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/23 22:17:23 by azahino-          #+#    #+#             #
#    Updated: 2026/09/23 22:17:23 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from alchemy import grimoire

print(
    f"{grimoire.light_spell_record("Fantasy", "earth, sun and gold")}"
    "\n"
    f"{grimoire.light_spell_record("Fantasy", "sun and gold")}"
    "\n"
    f"{grimoire.dark_spell_record("Fantasy", "bats and frogs")}"
    "\n"
    f"{grimoire.light_spell_record("Fantasy", "sun and gold")}"
    )
