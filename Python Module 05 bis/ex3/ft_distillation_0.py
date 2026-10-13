#!/usr/bin/env python3

from alchemy import potions

if __name__ == "__main__":
    print(
        "=== Distillation 0 ===\n"
        "Direct acces to alchemy/potions.py\n"
        f"Testing strength_potion: {potions.strength_potion()}\n"
        "Testin healing_potion:", potions.healing_potion()
    )
