from alchemy import elements
from .. import potions as p


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew"
        f"'{elements.create_air()}' and '{p.strength_potion()}'"
        f"mixed with '{elements.create_fire()}'"
    )
