#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message="There was an unknown error.") -> None:
        self.error = message


def water_plant(plant_name: str) -> None:
    name = plant_name
    if name == plant_name.capitalize():
        print(f"{plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: {plant_name}")


def test_watering_system() -> None:
    print("You have open watering system!\n")
    try:
        water_plant("Tomate")
        water_plant("PotAto")
        water_plant("Lettuce")
        print("\nAll plants have been watered!")
    except PlantError as error:
        print(f"PlantError detected: {error}\n")
    finally:
        print("Closing watering system...")

if __name__ == "__main__":
    test_watering_system()
