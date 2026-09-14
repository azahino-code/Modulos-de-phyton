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
try:
    test = alchemy.Element
    print(f"testing create_air: {test.air}")