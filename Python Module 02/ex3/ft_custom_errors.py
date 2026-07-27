# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_custom_errors.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/27 09:29:50 by azahino-          #+#    #+#             #
#    Updated: 2026/07/27 09:29:51 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class GardenError(Exception):
    def __init__(self, message="Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error") -> None:
        super().__init__(message)


def check_garden(water_day: int, litre: int) -> None:
    try:
        if water_day > 2:
            raise GardenError("The plant is wilting!")
        elif litre > 10:
            raise GardenError("Not enough water in the tank!")
        else:
            print("it's okey.")
    except GardenError as error:
        print(f"Caught GardenError: {error}")


def check_plant(wilting: int) -> None:
    try:
        if wilting > 2:
            raise PlantError("The plant is wilting!")
        elif wilting <= 2:
            print("The plant dont need any watering.")
        elif wilting is False:
            raise PlantError()
    except PlantError as error:
        print(f"Caught PlantError: {error}")


def check_water(litre: int) -> None:
    try:
        if litre > 10:
            raise WaterError("Not enough water in the tank!")
        elif litre <= 10:
            print("The tank don't need more water now, maybe later.")
        elif litre is False:
            raise WaterError()
    except WaterError as error:
        print(f"Caught WaterError: {error}")


print("=== Custom Garden Errors Demo ===\n")
print("Testing GardenError...")
check_garden(3, 8)
check_garden(3, 34)
check_garden(1, 9)
print("\nTestin PlantError...")
check_plant(1)
check_plant(5)
print("\nTestin WaterError...")
check_water(5432)
check_water(3)
print("\nAll custom error types work correctly!")
