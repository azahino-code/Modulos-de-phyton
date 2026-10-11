#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: str, days: str) -> None:
        self.name = name
        self.heigh = cm
        self.age = days

    def show(self) -> None:
        print(f"{self.name}: {self.heigh}cm, {self.age} days old")


if __name__ == "__main__":
    plant1: Plant = Plant("rose", "25", "30")
    plant2: Plant = Plant("Sunflower", "80", "45")
    plant3: Plant = Plant("Cactus", "15", "120")
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()
