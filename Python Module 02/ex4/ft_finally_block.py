# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_finally_block.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/27 19:14:20 by azahino-          #+#    #+#             #
#    Updated: 2026/07/27 19:14:21 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class PlantError(Exception):
    def __init__(self, message="There was an unknown error.") -> None:
        self.error = message


def water_plant(plant_name: str) -> None:
    name = plant_name
    if name == plant_name.capitalize():
        print(f"{plant_name} is watered!")
    else:
        raise PlantError(f"{plant_name} is not capitalized.")


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


test_watering_system()
