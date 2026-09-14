# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_alembic_3.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/14 19:23:38 by azahino-          #+#    #+#             #
#    Updated: 2026/09/14 19:23:45 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from alchemy import elements

test = elements.create_air()
print("=== Alembic 3 ===")
print("Accessing alchemy/elements.py using 'from ... import ...' structure")
print(f"Testing create_air: {test}")
