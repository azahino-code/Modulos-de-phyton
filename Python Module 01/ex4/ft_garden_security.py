# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_garden_security.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/22 15:59:21 by azahino-          #+#    #+#             #
#    Updated: 2026/07/22 15:59:34 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, cm, age) -> None:
        self.name = name
        self.height = float(cm)
        self.ages = int(age)

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
        return f"{self.name}: {round(self.height, 2)}cm, {self.ages} days old"


print("=== Garden Security Sistem ===")
plant1 = Plant("Rose", 15.0, 10)
print("Plant created: ", plant1.show(), "\n")
plant1.set_height(25)
plant1.set_age(30)
plant1.set_height(-25)
plant1.set_age(-30)
print("Current state: ", plant1.show())
