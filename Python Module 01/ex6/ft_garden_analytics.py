#!/usr/bin/env python3

class Plant:

    class Stadistic:
        def __init__(self):
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

    def __init__(self, name, height, ages) -> None:
        self.name = name
        self.height = float(height)
        self.ages = int(ages)
        self._stats = Plant.Stadistic()

    def grow(self, growth) -> None:
        self.height += growth
        self._stats._grow_calls += 1

    def age(self) -> None:
        self.ages += 1
        self._stats._age_calls += 1

    def set_height(self, new_height) -> None:
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self.height = new_height
            print(f"Height updated: {self.height}cm")

    def set_age(self, new_age) -> None:
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self.ages = new_age
            print(f"Age updated: {self.ages} days")

    @staticmethod
    def static_method(time) -> None:
        if time < 365:
            print(f"{time} is more than a year? -> FALSE")
        else:
            print(f"{time} is more than a year? -> TRUE")

    @classmethod
    def anonymous(cls) -> Plant:
        return cls("Anonymous", 0, 0)

    def get_height(self) -> None:
        print(f"{self.name}: actual height: {self.height}cm")

    def get_age(self) -> None:
        print(f"{self.ages}: actual age: {self.ages} days old")

    def show(self) -> str:
        self._stats._show_calls += 1
        return f"{self.name}: {round(self.height, 1)}cm, {self.ages} days old"


class Tree(Plant):
    def __init__(self, name, height, ages, trunk_diameter) -> None:
        super().__init__(name, height, ages)
        self.trunk_diameter = trunk_diameter
        self._produced_shades = 0

    def produce_shade(self) -> None:
        self._produced_shades += 1
        print(f"[Asking the {self.name} to produce shade]")
        str1 = f"Tree {self.name} now produces a shade of"
        str2 = f" {self.height}cm long and {self.trunk_diameter}cm wide"
        print(str1 + str2)

    def show(self) -> str:
        text = super().show()
        return (
            text + '\n' + f"Diameter: {round(self.trunk_diameter, 1)}cm"
            )


class Flower(Plant):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages)
        self.color = color
        self.is_blooming = False

    def ask_bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> str:
        text = super().show()
        text = text + '\n' + f"Color: {self.color}\n"
        if self.is_blooming:
            return (
                text + f"{self.name} is blooming beautifully!"
                )
        else:
            return (
                text + f"{self.name} has not bloomed yet"
                )


class Seed(Flower):
    def __init__(self, name, height, ages, color, n_seeds):
        super().__init__(name, height, ages, color)
        self.seeds_number = n_seeds

    def ask_bloom(self, seeds: int) -> None:
        super().ask_bloom()
        self.seeds_number = self.seeds_number + seeds

    def show(self) -> str:
        text = super().show()
        return text + f"\nseeds: {self.seeds_number}"


class Vegetable(Plant):
    def __init__(self, name, height, ages, harvest_season, nutritional_value):
        super().__init__(name, height, ages)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow_up(self, days) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        i = 0
        for i in range(days):
            super().grow(1)
            super().age()
            self.nutritional_value += 1

    def show(self) -> str:
        text = super().show()
        text = text = '\n' + f"Season: {self.harvest_season}\n"
        return text + f"Nutritional value: {self.nutritional_value}."


def show_stats(plant: Plant) -> None:
    if isinstance(plant, Tree):
        print(
            f"[stadistics for {plant.name}]\n",
            "Stats: " + str(plant._stats._grow_calls),
            "grow " + str(plant._stats._age_calls),
            "age " + str(plant._stats._show_calls) + " show",
            f"\n {plant._produced_shades} shade"
    )
    else:
        print(
            f"[stadistics for {plant.name}]\n",
            "Stats: " + str(plant._stats._grow_calls),
            "grow " + str(plant._stats._age_calls),
            "age " + str(plant._stats._show_calls) + " show"
        )


if __name__ == "__main__":
    print(
        "=== Garden stadistic ===\n=== Check year-old"
	)
    plant = Flower("Rose", 25, 10, "red")
    plant.static_method(30)
    plant.static_method(400)
    print(
        "\n=== Flower\n" + plant.show()
	)
    show_stats(plant)
    print("[asking the rose to grow an bloom]")
    plant.grow(10)
    plant.ask_bloom()
    print(plant.show())
    show_stats(plant)
    
    tree = Tree("Oak", 100, 365, 25)
    print(
        "\n===Tree\n" + tree.show(),
        "[asking the oak to produce shade]"
    )
    tree.produce_shade()
    show_stats(tree)
    seed = Seed("Sunflower", 80, 45, "yellow", 0)
    print("\n=== Seed")
    print(seed.show())
    print("[make sunflower grow, age and bloom]")
    seed.grow(55)
    seed.age()
    seed.ask_bloom(42)
    print(seed.show())
    anonimous = Plant.anonymous()
    print(
        "\n=== Anonymous\n",
        anonimous.show()
	)
    show_stats(anonimous)
