#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.error = message


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        self.error = message


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        self.error = message


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


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    print("Testin PlantError...")
    check_plant(1)
    check_plant(5)
    print("\nTestin WaterError...")
    check_water(5432)
    check_water(3)
    print("\nTesting catching all garden error...")
    check_garden(3, 8)
    check_garden(1, 34)
    check_garden(1, 9)
    print("\nAll custom error types work correctly!")
