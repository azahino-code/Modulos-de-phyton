import alchemy.elements

elements = alchemy.elements


def healing_potion() -> str:
    return (
        "Healing potion brewed with "
        f"'{elements.create_earth()}' and '{elements.create_air()}'"
    )


def strength_potion() -> str:
    return (
        "Strength potion brewed with "
        f"'{elements.create_fire()}' and '{elements.create_water()}'"
    )
