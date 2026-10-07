#!/usr/bin/env python3

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
            print(
				self.name + ": Error, height can't be negative."
				"\nHeight update rejected."
			)
        else:
            self.height = new_height
            print("Height updated: " + str(self.height) + " cm")

    def set_age(self, new_age) -> None:
        if new_age < 0:
            print(
                self.name + ": Error, age can't be negative."
                "\nAge update rejected."
			)
        else:
            self.ages = new_age
            print(
                f"Age updated: {str(self.ages)} days"
            )

    def get_height(self) -> None:
        print(
            self.name + ": actual height: ",
            str(self.height) + "cm."
        )

    def get_age(self) -> None:
        print(
            self.ages + " actual age: ",
            str(self.ages) + " days old."
        )

    def show(self) -> str:
        h = round(self.height, 2)
        return (
            f"{self.name}: {str(h)}cm, {str(self.ages)} days old"
		)


if __name__ == "__main__":
    print("=== Garden Security Sistem ===")
    plant1 = Plant("Rose", 15.0, 10)
    print("Plant created: ", plant1.show(), "\n")
    plant1.set_height(25)
    plant1.set_age(30)
    print()
    plant1.set_height(-25)
    plant1.set_age(-30)
    print(f"\nCurrent state:  {plant1.show()}")
