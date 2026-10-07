#!/usr/bin/env python3

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
