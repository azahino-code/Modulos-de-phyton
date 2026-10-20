#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, ages: int) -> None:
        self._name: str = name
        self._height: float = 0.0
        self._growth: float = 0.0
        self._ages: int = 0
        self.set_height(height)
        self.set_age(ages)

    def grow(self, growth: float) -> None:
        if growth + self._height < 0:
            print(f"{self._name}: Error, growth can't be negative")
            print("Growth rejected")
        else:
            self._height += growth
            self._growth += growth

    def age(self) -> None:
        self._ages += 1

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative.")
            print("Height update rejected.")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative.")
            print("Age update rejected.")
        else:
            self._ages = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._ages

    def show(self) -> str:
        return (
            f"{self._name}: {round(self._height, 1)}cm,"
            f"{self._ages} days old"
        )


class Tree(Plant):
    def __init__(
        self, name: str, height: float, ages: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, ages)
        self._trunk_diameter: float = trunk_diameter

    def produce_shade(self) -> None:
        print(f"[Asking the {self._name} to produce shade]")
        str1 = f"Tree {self._name} now produces a shade of"
        str2 = f" {self._height}cm long and {self._trunk_diameter}cm wide."
        print(str1 + str2)

    def show(self) -> str:
        text = super().show()
        return (
            text + '\n' + f"Diameter: {round(self._trunk_diameter, 1)}cm."
            )


class Flower(Plant):
    def __init__(
        self, name: str, height: float,
        ages: int, color: str
    ) -> None:
        super().__init__(name, height, ages)
        self._color: str = color
        self._is_blooming: bool = False

    def bloom(self) -> None:
        print(f"[asking the {self._name} to bloom]")
        self._is_blooming = True

    def show(self) -> str:
        text = super().show()
        text = text + '\n' + f"Color: {self._color}.\n"
        if self._is_blooming:
            return (
                text + f"{self._name} is blooming beautifully!"
                )
        else:
            return (
                text + f"{self._name} has not bloomed yet."
                )


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, ages: int,
        harvest_season: str, nutritional_value: float
    ) -> None:
        super().__init__(name, height, ages)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def grow(self, growth: float) -> None:
        super().grow(growth)
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def show(self) -> str:
        text = super().show()
        text = text + '\n' + f"Harvest season: {self._harvest_season}.\n"
        return text + f"Nutritional value: {round(self._nutritional_value)}"


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    plant1 = Flower("Rose", 15, 10, "red")
    print(plant1.show())
    plant1.bloom()
    print(plant1.show())
    print("\n=== Tree")
    plant2 = Tree("Oak", 200, 365, 5)
    print(plant2.show())
    plant2.produce_shade()
    print("\n=== Vegetable")
    plant3 = Vegetable("Tomato", 5, 10, "April", 0)
    print(plant3.show())
    for i in range(20):
        plant3.grow(3)
        plant3.age()
    print(plant3.show())
