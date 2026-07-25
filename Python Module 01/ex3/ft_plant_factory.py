# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_factory.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/22 15:17:41 by azahino-          #+#    #+#             #
#    Updated: 2026/07/22 15:18:09 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, starting_cm, starting_days):
        self.name = name
        self.height = float(starting_cm)
        self.ages = int(starting_days)

    def grow(self):
        self.height += 2

    def age(self):
        self.ages += 1

    def show(self):
        print(f"created: {self.name}: {self.height}cm, {self.ages} days old")


plant1 = Plant("rose", 25.6, 30)
plant2 = Plant("Oak", 200.0, 365)
plant3 = Plant("Cactus", 200.0, 90)
plant4 = Plant("Sunflower", 80.0, 45)
plant5 = Plant("Fern", 15.0, 120)

print("=== Plant Factory Output ===")
plant1.show()
plant2.show()
plant3.show()
plant4.show()
plant5.show()
