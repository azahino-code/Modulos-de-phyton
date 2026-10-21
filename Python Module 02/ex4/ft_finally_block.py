#!/usr/bin/env python3

class PlantError(Exception):
    def __init__(self, message: str = "") -> None:
        self.error = message

    def __str__(self) -> str:
        return self.error


def water_plant(plant_name: str) -> None:
    if plant_name == plant_name.capitalize():
        print(f"{plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:
    vault1 = ["Tomato", "Lettuce", "Carrots"]
    vault2 = ["Tomato", "lettuce", "Carrot"]
    print("=== Garden Watering System ===\n")
    try:
        print("Testing valid plants...")
        print("Opening watering system")
        for plant in vault1:
            water_plant(plant)
    except PlantError as error:
        print(
            f"PlantError detected: {error}\n"
            "... ending test and returnin to main\n"
        )
    finally:
        print("Closing watering system...\n")

    try:
        print(
            "Testing invalid plants..."
            "\nOpening watering system"
        )
        for plant in vault2:
            water_plant(plant)
    except PlantError as error:
        print(
            f"PlantError detected: {error}\n"
            "... ending test and returning to main"
        )
    finally:
        print("Closing watering system...\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
