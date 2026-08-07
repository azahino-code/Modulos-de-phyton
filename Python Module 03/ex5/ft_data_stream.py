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


def gen_event(n: list[str], q: int) -> Generator[tuple[str, str], None, None]:
    ev = ["run", "climb", "swim", "roar", "lift", "leave", "joke", "speak"]
    i = 0
    while i < q:
        person_action: tuple[str, str] = (random.choice(n), random.choice(ev))
        yield person_action
        i += 1


def con_e(e) -> Generator[tuple[str, str], None, None]:
    while len(e):
        num = random.randint(0, len(e) - 1)
        retire = e.pop(num)
        yield retire


players: list[str] = ["Aritz", "Anne", "Julen", "Josune"]
i = 0
number_of_events = 1000
p_a = gen_event(players, number_of_events)
event_list: list[tuple[str, str]] = []
while i < number_of_events:
    player, action = next(p_a)
    print(f"event {i}: Player {player} did action {action}")
    i += 1

i = 0
new_gen = gen_event(players, 10)
while i < 10:
    player, action = next(new_gen)
    event_list.append((player, action))
    i += 1
print("Built list of 10 events: ", event_list)

erase_gen = con_e(event_list)
for retire in erase_gen:
    print(f"Got event from list: {retire}")
    print(f"Remains in list: {event_list}")
