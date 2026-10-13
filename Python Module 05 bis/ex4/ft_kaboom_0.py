#!usr/bin/env python3

from alchemy import grimoire


if __name__ == "__main__":
    print(
        "=== Kaboom 0 ===\n"
        "Using grimoire module directly\n"
        f"{grimoire.light_spell_record("Fantasy", "earth, wind and fire")}"
    )
