# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_growth.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: azahino- <azahino-@student.42urduliz.com>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/22 14:32:41 by azahino-           #+#    #+#             #
#   Updated: 2026/10/06 18:44:22 by azahino-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, cm, days):
        self.name = name
        self.height = float(cm)
        self.days = int(days)

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        h = round(plant.height, 3)
        str1 = plant.name + ": " + str(h)
        print(str1 + "cm, " + str(plant.days) + " days old")


if __name__ == "__main__":
    plant = Plant("rose", 0.32, 0)
    print("=== Garden Plant Growth ===")
    plant.show()
    i = 1
    for i in range(7):
        plant.grow()
        plant.age()
        print(f"=== Day {i} ===")
        plant.show()
