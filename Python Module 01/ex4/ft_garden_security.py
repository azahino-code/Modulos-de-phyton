#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, cm: float, age: int) -> None:
        self._name: str = name
        self._height = 0.0
        self._ages = 0
        self._growth = 0.0
        self.set_height(cm)
        self.set_age(age)

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
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._ages = new_age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._ages

    def show(self) -> str:
        h = round(self._height, 1)
        return (
            f"{self._name}: {str(h)}cm, {str(self._ages)} days old"
        )


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = Plant("Rose", 15.0, 10)
    print("Plant created: ", plant1.show(), "\n")
    plant1.set_height(25)
    plant1.set_age(30)
    print(
        f"Height updated: {plant1.get_height()}cm\n"
        f"Age updated: {plant1.get_age()} days\n"
    )
    plant1.set_height(-5)
    plant1.set_age(-30)
    print(f"\nCurrent state:  {plant1.show()}")
