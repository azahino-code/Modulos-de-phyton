# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_data_stream.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.co    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/03 12:19:54 by azahino-          #+#    #+#             #
#    Updated: 2026/08/03 12:19:55 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import random

from typing import Generator


def gen_event(names: list[str]) -> Generator[tuple[str, str], None, None]:
    ev = ["run", "climb", "swim", "roar", "lift", "leave", "joke", "speak"]
    i = 0
    while i <= 999:
        person_action: tuple[str, str] = (random.choice(names), random.choice(ev))
        yield person_action
        i += 1
    
# def consume_events():

players: list[str] = ["Aritz", "Anne", "Julen", "Josune"]
i = 0
p_a = gen_event(players)
event_list: list[str,str] = []
while i <= 999:
    player, action = next(p_a)
    if i < 10:
        event_list.append((player, action))
    print(f"event {i}: Player {player}, {action}")
    i += 1

print("Built list of 10 events: ", event_list)
