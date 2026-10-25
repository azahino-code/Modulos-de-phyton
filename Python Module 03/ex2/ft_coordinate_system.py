#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            text = input("Enter new coordinates as floats in format 'x,y,z':")
            str_x, str_y, str_z = text.strip().split(",")
            x = float(str_x)
            y = float(str_y)
            z = float(str_z)
            return (x, y, z)
        except ValueError:
            print("Invalid syntax")
            continue


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    c = get_player_pos()
    print(
        f"It includes: X={round(c[0], 2)},"
        f"Y={round(c[1], 2)}, Z={round(c[2])}"
    )
    res = math.sqrt((0 - c[0])**2 + (0 - c[1])**2 + (0 - c[2])**2)
    print(f"Distance to center: {res}\n")
    print("Get a second set of coordinates")
    c2 = get_player_pos()
    res = math.sqrt((c2[0] - c[0])**2 + (c2[1] - c[1])**2 + (c2[2] - c[2])**2)
    print(f"Distance between the 2 sets of coordinates: {round(res, 4)}")
