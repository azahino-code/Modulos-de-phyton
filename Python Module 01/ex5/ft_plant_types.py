# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_types.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/23 15:29:56 by azahino-          #+#    #+#             #
#    Updated: 2026/07/23 15:30:08 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, height, ages):
        self.name = name
        self.height = float(height)
        self.ages = int(ages)

    def grow(self, growth):
        self.height += growth

    def age(self):
        self.ages += 1

    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative.")
            print("Height update rejected.")
        else:
            self.height = new_height
            print(f"Height updated: {self.height}cm")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative.")
            print("Age update rejected.")
        else:
            self.ages = new_age
            print(f"Age updated: {self.ages} days")

    def get_height(self):
        print(f"{self.name}: actual height: {self.height}cm.")

    def get_age(self):
        print(f"{self.ages}: actual age: {self.ages} days old.")

    def show(self):
        return f"{self.name}: {round(self.height, 1)}cm, {self.ages} days old"


class Tree(Plant):
    def __init__(self, name, height, ages, trunk_diameter):
        super().__init__(name, height, ages)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        print(f"[Asking the {self.name} to produce shade]")
        str1 = f"Tree {self.name} now produces a shade of"
        str2 = f" {self.height}cm long and {self.trunk_diameter}cm wide."
        print(str1 + str2)

    def show(self):
        print(super().show())
        print(f"Diameter: {round(self.trunk_diameter, 1)}cm.")


class Flower(Plant):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages)
        self.color = color
        self.bloom = False

    def ask_bloom(self):
        print(f"[Asking the {self.name} to bloom]")
        self.bloom = True

    def show(self):
        print(super().show())
        print(f"Color: {self.color}.")
        if self.bloom:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet.")


class Vegetable(Plant):
    def __init__(self, name, height, ages, harvest_season, nutritional_value):
        super().__init__(name, height, ages)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow_up(self, days):
        print(f"[make {self.name} grow and age for {days} days.]")
        i = 0
        for i in range(days):
            super().grow(1)
            super().age()
            self.nutritional_value += 1

    def show(self):
        print(super().show())
        print(f"Season: {self.harvest_season}.")
        print(f"Nutritional value: {self.nutritional_value}.")


print("=== Garden Plant Types ===")
print("=== Flower")
plant1 = Flower("Rose", 15, 10, "red")
plant1.show()
plant1.ask_bloom()
plant1.show()
print("\n=== Tree")
plant1 = Tree("Oak", 200, 365, 5)
plant1.show()
plant1.produce_shade()
print("\n=== Vegetable")
plant1 = Vegetable("Tomato", 5, 10, "April", 0)
plant1.show()
plant1.grow_up(20)
plant1.show()
