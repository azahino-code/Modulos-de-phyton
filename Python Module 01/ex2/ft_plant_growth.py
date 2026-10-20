#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: float, days: int):
        self.name: str = name
        self.height: float = cm
        self.growth: float = 0.0
        self.days: int = days

    def grow(self, growth: float) -> None:
        if growth + self.height < 0:
            print(f"{self.name}: Error, growth can't be negative")
            print("Growth rejected")
        else:
            self.height += growth
            self.growth += growth

    def age(self) -> None:
        self.days += 1

    def show(self) -> None:
        str1 = f"{plant.name}: {round(plant.height, 1)}"
        print(str1 + f"cm, {plant.days} days old")


if __name__ == "__main__":
    plant = Plant("rose", 0.32, 0)
    print("=== Garden Plant Growth ===")
    plant.show()
    i = 1
    for i in range(7):
        plant.grow(3.5)
        plant.age()
        print(f"=== Day {i} ===")
        plant.show()
    print(f"Growth this week: {round(plant.growth, 1)}cm")
