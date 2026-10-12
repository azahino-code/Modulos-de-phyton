#!/usr/bin/env python3

import math


def get_player_pos(trys: int) -> tuple[float, ...]:
    try:
        text = input("Enter new coordinates as floats in format 'x,y,z':")
        text = text.strip()
        str_x, str_y, str_z = text.split(",")

    except ValueError:
        print("Invalid syntax")
        return get_player_pos(trys + 1)
    values = [str_x, str_y, str_z]
    coordis = []
    for value in values:
        try:
            coordis.append(float(value))
        except ValueError:
            print(
                f"Error on parameter '{value}': "
                "could not convert string to float"
            )
            return get_player_pos(trys + 1)
    coor = tuple(coordis)
    if trys > 0:
        print(f"Number of trys: {trys}")
    return coor


print("=== Game Coordinate System ===\n")
print("Get a first set of coordinates")
c = get_player_pos(0)
print(f"It includes: X={round(c[0], 2)}, Y={round(c[1], 2)}, Z={round(c[2])}")
res = math.sqrt((0 - c[0])**2 + (0 - c[1])**2 + (0 - c[2])**2)
print(f"Distance to center: {res}\n")
print("Get a second set of coordinates")
c2 = get_player_pos(0)
res = math.sqrt((c2[0]-c[0])**2 + (c2[1]-c[1])**2 + (c2[2]-c[2])**2)
print(f"Distance between the 2 sets of coordinates: {round(res, 4)}")
