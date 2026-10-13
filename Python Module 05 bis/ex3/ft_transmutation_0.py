#!/usr/bin/env python3

import alchemy.transmutation.recipes as recipe


if __name__ == "__main__":
    print(
        "=== Transmutation 0 ===\n"
        "Using file alchemy/transmutation/recipes.py directly\n"
        f"Testing lead to gold: {recipe.lead_to_gold()}"
    )
