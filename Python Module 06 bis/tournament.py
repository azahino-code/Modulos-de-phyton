#!/usr/bin/env python3

from ex3 import (
    TransformationFactory,
    FireFactory,
    CreatureFactory
)
from ex4 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError
)


def battle(fighters: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    base_1 = fighters[0][0].create_base()
    base_2 = fighters[1][0].create_base()
    print(
        f"{base_1.describe()}",
        " vs.",
        f"{base_2.describe()}",
        " now fight",
        sep="\n"
    )
    for mons, strat in fighters:
        beast = mons.create_base()
        strat.act(beast)


if __name__ == "__main__":
    parts: list[tuple[CreatureFactory, BattleStrategy]] = [
        (FireFactory(), NormalStrategy()),
        (TransformationFactory(), AggressiveStrategy())
    ]
    print(
        "Tournament 0 (basic)",
        "[ (Flameling+Normal), (Shiftling+Aggressive) ]",
        "*** Tournament ***",
        "2 opponents involved\n",

        "* Battle *",
        sep="\n"
    )
    battle(parts)
    parts = [
        (TransformationFactory(), AggressiveStrategy()),
        (FireFactory(), AggressiveStrategy()),
    ]
    print(
        "\nTournament 1 (error)",
        "[ (Shiftling+Aggressive), (Flameling+Aggressive) ]",
        "*** Tournament ***",
        "2 opponents involved\n",
        "* Battle *",
        sep="\n"
    )
    try:
        battle(parts)
    except InvalidStrategyError as e:
        print(f"An error occurred: {e}")
