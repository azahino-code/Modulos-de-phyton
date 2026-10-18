#!/usr/bin/env python3

from ex3 import (
    CreatureFactory,
    FireFactory,
    TransformationFactory
)


def creation(fac: CreatureFactory) -> None:
    base = fac.create_base()
    evolved = fac.create_evolved()

    print(
        f"{base.describe()}\n"
        f"{base.attack()}"
    )
    print(
        f"{evolved.describe()}\n"
        f"{evolved.attack()}" 
    )


def battle(
    monster_1: CreatureFactory,
    monster_2: CreatureFactory
) -> None:
    base_1 = monster_1.create_base()
    base_2 = monster_2.create_base()

    print(
        f"{base_1.describe()}\n"
        " vs.\n"
        f"{base_2.describe()}\n"
        " fight!\n"
        f"{base_1.attack()}\n"
        f"{base_2.attack()}"
    )


if __name__ == "__main__":
    print("Testing factory")
    creation(FireFactory())

    print("\nTesting factory")
    creation(TransformationFactory())

    print("\nTesting battle")
    battle(FireFactory(), TransformationFactory())
