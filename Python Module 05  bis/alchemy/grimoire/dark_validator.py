from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for key in dark_spell_allowed_ingredients():
        if key in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
