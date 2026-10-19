#!/usr/bin/env python3

from ex3 import (
    TransformationFactory,
    FireFactory, 
    CreatureFactory
)
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy
)

def battle(fighters: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    base_1 = fighters[0][0].create_base()
    base_2 = fighters[0][0].create_base()
    print(
        f"{base_1.describe()}",
        " vs.",
        f"{base_2.describe()}",
        " now fight",
        sep = "\n"
    )
    for mons in fighters:
        base = mons[0].create_base()
        mons[1].act()


if __name__ == "__main__":
    parts: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FireFactory(), NormalStrategy(FireFactory().create_base())),
        (TransformationFactory(), AggressiveStrategy(TransformationFactory().create_base()))
    ]
    print(
        "Tournament 0 (basic)",
        "[ (Flameling+Normal), (Shiftling+Aggressive) ]",
        "*** Tournament ***",
        "2 opponents involved\n",

        "* Battle *",
        sep = "\n"
    )
    battle(parts)
    parts = [
        (TransformationFactory(), AggressiveStrategy(TransformationFactory().create_base())),
        (FireFactory(), AggressiveStrategy(FireFactory().create_base())),
    ]
    print(
        "\nTournament 1 (error)",
        "[ (Shiftling+Aggressive), (Flameling+Aggressive) ]",
        "*** Tournament ***",
        "2 opponents involved\n",
        "* Battle *",
        sep = "\n"
    )
    battle(parts)
