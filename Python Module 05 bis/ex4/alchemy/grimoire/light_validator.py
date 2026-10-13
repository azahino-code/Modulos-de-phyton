def validate_ingredients(ingredients: str) -> str:
    from alchemy.grimoire.light_spellbook import (
        light_spell_allowed_ingredients,
    )
    for key in light_spell_allowed_ingredients():
        if key in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
