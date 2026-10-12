#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str = "") -> None:
        ...


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"{plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        water_plant("Tomat")
        water_plant("Lettuce")
        water_plant("Carrots")

    except PlantError as error:
        print(
            f"PlantError detected: {error}\n" +
            "... ending test and returnin to main\n"
        )

    try:
        print(
            "\nTesting invalid plants...\nOpening watering system"
        )
        water_plant("Tomato")
        water_plant("lettuce")
        water_plant("Carrot")

    except PlantError as error:
        print(
            f"PlantError detected: {error}\n" +
            "... ending test and returnin to main\n"
        )
    finally:
        print("Closing watering system...\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
