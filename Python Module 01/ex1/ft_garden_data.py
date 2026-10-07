#!/usr/bin/env python3

class Plant:
    def __init__(self, name, cm, days):
        self.name = name
        self.heigh = cm
        self.age = days

    def show(self) -> None:
        print(f"{self.name}: {self.heigh}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("rose", "25", "30")
    plant2 = Plant("Sunflower", "80", "45")
    plant3 = Plant("Cactus", "15", "120")
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
