#!/usr/bin/env python3

import random


class Player:
    def __init__(self, name: str, achievements: set[str]) -> None:
        self.name = name
        self.ach = achievements


def gen_player_achievements(achievement: list[str]) -> set[str]:
    a_num = random.randint(1, len(achievement))
    player_achivs: set[str] = set()
    while len(player_achivs) < a_num:
        player_achivs.add(random.choice(achievement))
    return player_achivs


if __name__ == "__main__":
    achievement = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    
    a = Player("Anne", gen_player_achievements(achievement))
    b = Player("Rod", gen_player_achievements(achievement))
    c = Player("Bob", gen_player_achievements(achievement))
    d = Player("d", gen_player_achievements(achievement))
    players: list[Player] = [a, b, c, d]
    all_ach: set[str] = set()
    for player in players:
        print(f"Player {player.name}: {player.ach}")
        all_ach.update(player.ach)
    print(f"\nAll distinct achievements: {all_ach}")
    common = players[0].ach.intersection(*(player.ach for player in players[1:]))
    print(f"Common achieves: {common}\n")
    for player in players:
        others = set(players) - {player}
        others_ach: set[str] = set()
        for other in others:
            others_ach.update(other.ach)
        print(f"Only {player.name} has: {player.ach.difference(others_ach)}")
    for player in players:
        print(f"\n{player.name} is missing: {all_ach.difference(player.ach)}")
