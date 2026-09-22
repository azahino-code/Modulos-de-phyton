# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_alembic_4.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/14 19:30:13 by azahino-          #+#    #+#             #
#    Updated: 2026/09/14 19:30:14 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import alchemy

print("=== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy")

print(alchemy.create_air())

print("Now show that not all functions can be reached")
print("This will raise an exception!")
print("Testing the hidden create_earth: ", end="")
print(alchemy.create_earth())
