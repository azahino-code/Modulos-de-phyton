# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_alembic_1.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/12 01:00:05 by azahino-          #+#    #+#             #
#    Updated: 2026/09/12 01:00:06 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from elements import create_water

test = create_water()
print("=== Alembic 1 ===")
print("Using: 'from ... import ...' structure to access elements.py")
print(f"Testing create_water: {test}")
