# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_coordinate_system.py                            :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/01 21:15:58 by azahino-          #+#    #+#             #
#    Updated: 2026/08/01 21:15:59 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import math

def get_player_pos(trys: int) -> tuple:
    try:
        text = input("Enter new coordinates as floats in format 'x,y,z':")
        x, y, z = text.split(",")
        x = float(x)
        y = float(y)
        z = float(z)
        coor = (x, y, z)
        if len(coor) != 3:
            raise ValueError("Invalid sintax")
        return coor
    except ValueError as error:
        print(f"{error}")
        return(get_player_pos(trys + 1))
    finally:
        print(f"Number of trys: {trys}")


print("=== Game Coordinate System ===\n")
print("Get a first set of coordinates")
c = get_player_pos(1)
print(f"It includes: X={round(c[0], 2)}, Y={round(c[1], 2)}, Z={round(c[2])}")
res = math.sqrt(0 - c[0]**2 + (0 - c[1])**2 + (0 - c[2])**2)
print(f"Distance to center: {res}\n")
print("Get a second set of coordinates")
c2 = get_player_pos(1)
res = math.sqrt(c2[0]-c[0]**2+(c2[1]-c[1])**2+(c2[2]-c[2])**2)
