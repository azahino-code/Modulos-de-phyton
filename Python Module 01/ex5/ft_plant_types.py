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
    def __init__(self, name, height, ages) -> None:
        self.name = name
        self.height = float(height)
        self.ages = int(ages)

    def grow(self, growth) -> None:
        self.height += growth

    def age(self) -> None:
        self.ages += 1

    def set_height(self, new_height) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative.")
            print("Height update rejected.")
        else:
            self.height = new_height
            print(f"Height updated: {self.height}cm")

    def set_age(self, new_age) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative.")
            print("Age update rejected.")
        else:
            self.ages = new_age
            print(f"Age updated: {self.ages} days")

    def get_height(self) -> None:
        print(f"{self.name}: actual height: {self.height}cm.")

    def get_age(self) -> None:
        print(f"{self.ages}: actual age: {self.ages} days old.")

    def show(self) -> str:
        return f"{self.name}: {round(self.height, 1)}cm, {self.ages} days old"


class Tree(Plant):
    def __init__(self, name, height, ages, trunk_diameter) -> None:
        super().__init__(name, height, ages)
        self.trunk_diameter = trunk_diameter

    def pbuce_shade(self) -> None:
        print(f"[Asking the {self.name} to pbuce shade]")
        str1 = f"Tree {self.name} now pbuces a shade of"
        str2 = f" {self.height}cm long and {self.trunk_diameter}cm wide."
        print(str1 + str2)

    def show(self) -> str:
        text = super().show()
        return (
            text + '\n' + f"Diameter: {round(self.trunk_diameter, 1)}cm."
            )


class Flower(Plant):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages)
        self.color = color
        self.bloom = False

    def ask_bloom(self) -> None:
        print(f"[Asking the {self.name} to bloom]")
        self.bloom = True

    def show(self) -> str:
        text = super().show()
        text = text + '\n' + f"Color: {self.color}.\n"
        if self.bloom:
            return (
                text + f"{self.name} is blooming beautifully!"
                )
        else:
            return (
                text + f"{self.name} has not bloomed yet."
                )


class Vegetable(Plant):
    def __init__(self, name, height, ages, harvest_season, nutritional_value):
        super().__init__(name, height, ages)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow_up(self, days) -> None:
        print(f"[make {self.name} grow and age for {days} days.]")
        i = 0
        for i in range(days):
            super().grow(1)
            super().age()
            self.nutritional_value += 1

    def show(self) -> str:
        text = super().show()
        text = text = '\n' + f"Season: {self.harvest_season}.\n"
        return text + f"Nutritional value: {self.nutritional_value}."


print("=== Garden Plant Types ===")
print("=== Flower")
plant1 = Flower("Rose", 15, 10, "red")
print(plant1.show())
plant1.ask_bloom()
print(plant1.show())
print("\n=== Tree")
plant2 = Tree("Oak", 200, 365, 5)
print(plant2.show())
plant2.pbuce_shade()
print("\n=== Vegetable")
plant3 = Vegetable("Tomato", 5, 10, "April", 0)
print(plant3.show())
plant3.grow_up(20)
print(plant3.show())
