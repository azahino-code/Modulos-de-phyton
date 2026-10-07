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
            print({self.name} + ": Error, height can't be negative.")
            print("Height update rejected.")
        else:
            self.height = new_height
            print("Height updated: " + self.height + "cm")

    def set_age(self, new_age) -> None:
        if new_age < 0:
            print(self.name + ": Error, age can't be negative.")
            print("Age update rejected.")
        else:
            self.ages = new_age
            print("Age updated: " + self.ages + " days")

    @staticmethod
    def static_method(time: int) -> None:
        if time < 365:
            print("Is " + str(time) + " more than a year? -> FALSE")
        else:
            print("Is " + str(time) + " is more than a year? -> TRUE")

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Anonymous", 0, 0)

    def get_height(self) -> None:
        print(self.name + ": actual height: {self.height}cm.")

    def get_age(self) -> None:
        print(self.ages + ": actual age: {self.ages} days old.")

    def show(self) -> str:
        self._stats._show_calls += 1
        return self.name + ": {round(self.height, 1)}cm, {self.ages} days old"


class Tree(Plant):
    def __init__(self, name, height, ages, trunk_diameter) -> None:
        super().__init__(name, height, ages)
        self.trunk_diameter = trunk_diameter
        self._pbuced_shades = 0

    def pbuce_shade(self) -> None:
        self._pbuced_shades += 1
        print("[Asking the " + self.name + "to pbuce shade]")
        str1 = "Tree " + self.name + "now pbuces a shade of "
        str2 =  str(self.height) + "cm long and "
        print(str1 + str2 + str(self.trunk_diameter) + "cm wide.")

    def show(self) -> str:
        text = super().show()
        diameter = round(self.trunk_diameter, 1)
        return (
            text + '\n' + "Diameter: " + str(diameter) + "cm."
            )


class Flower(Plant):
    def __init__(self, name, height, ages, color):
        super().__init__(name, height, ages)
        self.color = color
        self.is_blooming = False

    def ask_bloom(self) -> None:
        print("[Asking the " + self.name + " to bloom]")
        self.is_blooming = True

    def show(self) -> str:
        text = super().show()
        text = text + '\n' + "Color: " + self.color + ".\n"
        if self.is_blooming:
            return (
                text + self.name + " is blooming beautifully!"
                )
        else:
            return (
                text + self.name + " has not bloomed yet."
                )


class Seed(Flower):
    def __init__(self, name, height, ages, color, n_seeds):
        super().__init__(name, height, ages, color)
        self.seeds_number = n_seeds

    def show(self) -> str:
        text = super().show()
        return (
            text + "\n" + self.name + ": seeds: ",
            str(self.seeds_number) + "."
		)


class Vegetable(Plant):
    def __init__(self, name, height, ages, harvest_season, nutritional_value):
        super().__init__(name, height, ages)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def grow_up(self, days) -> None:
        print("[make " + self.name + " grow and age for " + {days} + " days.]")
        i = 0
        for i in range(days):
            super().grow(1)
            super().age()
            self.nutritional_value += 1

    def show(self) -> str:
        text = super().show()
        text = text = '\n' + "Season: " + self.harvest_season + ".\n"
        return text + "Nutritional value: " + self.nutritional_value + "."


def show_stats(plant: Plant) -> None:
    print(
        "Stats: " + str(plant._stats._grow_calls),
        "grow " + str(plant._stats._age_calls),
        "age " + str(plant._stats._show_calls) + " show"
    )
    if isinstance(Plant, Tree):
        print("Shade calls: " + Plant._pbuced_shades)


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
    
    tree = Tree("Oak", 100, 365, 25)
    print(
        "\n===Tree\n" + tree.show(),
        "[asking the oak to produce shade]"
    )
    tree.pbuce_shade()
    show_stats(tree)
    seed = Seed("Sunflower", 80, 45, "yellow", 0)
    print("=== Seed\n")
    print(seed.show())
    print("[make sunflower grow, age and bloom]")
    seed.grow(55)
    seed.age()
    seed.ask_bloom()
    print(seed.show())
    anonimous = Plant.anonymous()
    print(
        "\n=== Anonymous\n",
        anonimous.show()
	)
    show_stats(anonimous)
