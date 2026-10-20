#!/usr/bin/env python3

class Plant:

    class Stadistics:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0
        
        def show_stats(self) -> None:
            print(
                f"Stats: {str(self._grow_calls)} grow, "
                f"{str(self._age_calls)} age, "
                f"{str(self._show_calls)} show"
            )

    def __init__(self, name: str, height: float, ages: int) -> None:
        self._name: str = name
        self._height: float = height
        self._growth: float = 0.0
        self._ages: int = ages
        self._stats: Plant.Stadistics = Plant.Stadistics()

    def grow(self, growth: float) -> None:
        if growth + self._height < 0:
            print(f"{self._name}: Error, growth can't be negative")
            print("Growth rejected")
        else:
            self._height += growth
            self._growth += growth
        self._stats._grow_calls += 1

    def age(self) -> None:
        self._ages += 1
        self._stats._age_calls += 1

    def set_height(self, new_height: float) -> None:
        if new_height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {round(self._height, 1)}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._ages = new_age
            print(f"Age updated: {self._ages} days")

    @staticmethod
    def static_method(time: int) -> None:
        if time < 365:
            print(f"{time} is more than a year? -> FALSE")
        else:
            print(f"{time} is more than a year? -> TRUE")

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> None:
        print(f"{self._name}: actual height: {round(self._height, 1)}cm")

    def get_age(self) -> None:
        print(f"{self._name}: actual age: {self._ages} days old")

    def show(self) -> str:
        self._stats._show_calls += 1
        return (
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._ages} days old"
            )


class Tree(Plant):
    def __init__(
        self, name: str, height: float,
        ages: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, ages)
        self._trunk_diameter: float = trunk_diameter
        self._produced_shades: int = 0

    def produce_shade(self) -> None:
        self._produced_shades += 1
        print(f"[asking the {self._name} to produce shade]")
        print(
            f"Tree {self._name} now produces a shade of"
            f" {round(self._height, 1)}cm long and"
            f" {round(self._trunk_diameter, 1)}cm wide"
        )

    def show(self) -> str:
        text = super().show()
        return (
            text + '\n' + f"Diameter: {round(self._trunk_diameter, 1)}cm"
            )


class Flower(Plant):
    def __init__(
        self, name: str, height: float,
        ages: int, color: str
    ) -> None:
        super().__init__(name, height, ages)
        self._color: str = color
        self._is_blooming: bool = False

    def ask_bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> str:
        text = super().show()
        text = text + '\n' + f"Color: {self._color}\n"
        if self._is_blooming is True:
            return (
                text + f"{self._name} is blooming beautifully!"
                )
        else:
            return (
                text + f"{self._name} has not bloomed yet"
                )


class Seed(Flower):
    def __init__(
        self, name: str, height: float, ages: int,
        color: str, n_seeds: int
    ) -> None:
        super().__init__(name, height, ages, color)
        self._seeds_number: int = n_seeds

    def show(self) -> str:
        text = super().show()
        if self._is_blooming is True:
            return text + f"\nSeeds: {self._seeds_number}"
        else:
            return text + "\nSeeds: 0"


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, ages: int,
        harvest_season: str, nutritional_value: int
    ) -> None:
        super().__init__(name, height, ages)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> str:
        text = super().show()
        text = text + '\n' + f"Season: {self._harvest_season}\n"
        return text + f"Nutritional value: {self._nutritional_value}."


def show_stats(plant: Plant) -> None:
    print(f"[stadistics for {plant._name}]")
    plant._stats.show_stats()
    if isinstance(plant, Tree):
        print(f"{plant._produced_shades} shades produced.")


if __name__ == "__main__":
    print(
        "=== Garden stadistic ===\n=== Check year-old"
        )
    plant = Flower("Rose", 15.0, 10, "red")
    plant.static_method(30)
    plant.static_method(400)
    print(
        "\n=== Flower\n" + plant.show()
        )
    show_stats(plant)
    print("[asking the rose to grow an bloom]")
    plant.grow(8)
    plant.ask_bloom()
    print(plant.show())
    show_stats(plant)

    tree = Tree("Oak", 100.0, 365, 5.0)
    print(
        "\n===Tree\n" + tree.show(),
        "[asking the oak to produce shade]"
    )
    tree.produce_shade()
    show_stats(tree)
    seed = Seed("Sunflower", 80.0, 45, "yellow", 42)
    print("\n=== Seed")
    print(seed.show())
    print("[make sunflower grow, age and bloom]")
    seed.grow(30)
    seed.age()
    seed.ask_bloom()
    print(seed.show())
    anonimous = Plant.anonymous()
    print(
        "\n=== Anonymous\n" + anonimous.show()
        )
    show_stats(anonimous)
