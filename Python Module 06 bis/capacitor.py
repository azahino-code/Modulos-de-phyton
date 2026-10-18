#!/usr/bin/env python3
from ex3 import TransformationFactory as t


base = t.create_base(t)
evolved = t.create_evolved(t)
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
    sep = ""
)

