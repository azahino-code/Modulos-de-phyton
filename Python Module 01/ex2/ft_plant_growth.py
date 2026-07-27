# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_growth.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/22 14:32:41 by azahino-          #+#    #+#             #
#    Updated: 2026/07/22 14:33:09 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, cm, days):
        self.name = name
        self.height = float(cm)
        self.days = int(days)

    def grow(self):
        self.height += 0.8

    def age(self):
        self.days += 1

    def show(self):
        str1 = f"{plant.name}: {round(plant.height, 2)}"
        print(str1 + f"cm, {plant.days} days old")


plant = Plant("rose", 0.32, 0)
print("=== Garden Plant Growth ===")
plant.show()
i = 1
for i in range(7):
    plant.grow()
    plant.age()
    print(f"=== Day {i} ===")
    plant.show()
