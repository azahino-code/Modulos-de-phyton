#!usr/bin/env python3

if __name__ == "__main__":
    print(
        "=== Kaboom 1 ===\n"
        "Access to alchemy/grimoire/dark_spellbook.py directly\n"
        "Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION"
    )

    from alchemy.grimoire import dark_spellbook
    print(f"Testing dark magic:  {dark_spellbook.dark_spell_record()}")
