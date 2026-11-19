#!/usr/bin/env python3
from typing import Protocol
from ex3 import TransformationFactory as T


class TransformableCreature(Protocol):
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        ...

    def transform(self) -> str:
        ...

    def revert(self) -> str:
        ...


if __name__ == "__main__":
    factory = T()
    base: TransformableCreature = factory.create_base()
    evolved: TransformableCreature = factory.create_evolved()
    print(
        "Testing Creature with transform capability\n",
        " base\n",
        f"{base.describe()}\n",
        f"{base.attack()}\n",
        f"{base.transform()}\n",
        f"{base.attack()}\n",
        f"{base.revert()}\n",
        " evolved:\n"
        f"{evolved.describe()}\n",
        f"{evolved.attack()}\n",
        f"{evolved.transform()}\n",
        f"{evolved.attack()}\n",
        f"{evolved.revert()}",
        sep=""
    )
