# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    data_alchemist.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/07 19:53:19 by azahino-          #+#    #+#             #
#    Updated: 2026/08/07 19:53:20 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import random


def capitalize_names(names: list[str]) -> list[str]:
    return_list = []
    for txt in names:
        return_list.append(txt.capitalize())
    return return_list


def only_caps(names: list[str]) -> list[str]:
    return_list = []
    for txt in names:
        if txt == txt.capitalize():
            return_list.append(txt.capitalize())
    return return_list


player_l = ['Anne', "bob", "Ca", "Dyl", "En", "Greg", "jon", "kev", "Liam"]
cap_list: list[str] = capitalize_names(player_l)
only_cap_list: list[str] = only_caps(player_l)

print(f"Initial list of players: {player_l}")

print(f"New list with all names capitalized: {cap_list}")

print(f"New list of capitalized names only: {only_cap_list}")

names_with_scores: dict = {}
for key in cap_list:
    names_with_scores[key] = random.randint(0, 1000)

print(f"Score dict: {names_with_scores}")
new_dict = {}
total = sum(names_with_scores.values()) / len(names_with_scores)
for key, value in names_with_scores.items():
    if value >= total:
        new_dict[key] = value

print(f"High scores: {new_dict}")
