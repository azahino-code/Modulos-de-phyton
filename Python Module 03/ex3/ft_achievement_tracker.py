# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_achievement_tracker                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/02 10:54:51 by azahino-          #+#    #+#             #
#    Updated: 2026/08/02 10:54:52 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import random


class Player:
    def __init__(self, name, achievements):
        self.name = name
        self.ach = achievements


def get_player_achievements(achievement: list[str]) -> set[str]:
    a_num = random.randint(1, len(achievement))
    ach_list: list[str] = []
    while len(ach_list) != a_num:
        ach_list.append(random.choice(achievement))
    player_achivs = set(ach_list)
    return player_achivs


achievement = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
all_ach: set[str] = set(achievement)
a = Player("Anne", get_player_achievements(achievement))
b = Player("Rod", get_player_achievements(achievement))
c = Player("Bob", get_player_achievements(achievement))
d = Player("d", get_player_achievements(achievement))
print(f"Player {a.name}: {a.ach}")
print(f"Player {b.name}: {b.ach}")
print(f"Player {c.name}: {c.ach}")
print(f"Player {d.name}: {d.ach}")
print(f"\nAll distinct achievements: {all_ach}")
common = all_ach.intersection(a.ach, b.ach, c.ach, d.ach)
print(f"Common achieve: {common}\n")

print(f"Only {a.name} has: {a.ach.difference(b.ach, c.ach, d.ach)}")
print(f"Only {b.name} has: {b.ach.difference(a.ach, c.ach, d.ach)}")
print(f"Only {d.name} has: {d.ach.difference(b.ach, c.ach, a.ach)}")
print(f"Only {c.name} has: {c.ach.difference(b.ach, a.ach, d.ach)}")

print(f"\n{a.name} is missing: {all_ach.difference(a.ach)}")
print(f"{b.name} is missing: {all_ach.difference(b.ach)}")
print(f"{c.name} is missing: {all_ach.difference(c.ach)}")
print(f"{d.name} is missing: {all_ach.difference(d.ach)}")
