#!/usr/bin/env python3

import random
from typing import Generator


def gen_event(names: list[str]) -> Generator[tuple[str, str], None, None]:
    events = [
        "run",
        "climb",
        "swim",
        "roar",
        "lift",
        "leave",
        "joke",
        "speak"
    ]
    while True:
        person_action: tuple[str, str] = (
            random.choice(names), random.choice(events)
        )
        yield person_action


def consume_event(
    event: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while len(event):
        num = random.randint(0, len(event) - 1)
        retire = event.pop(num)
        yield retire


if __name__ == "__main__":
    players: list[str] = ["Aritz", "Anne", "Julen", "Josune"]
    p_a = gen_event(players)
    event_list: list[tuple[str, str]] = []
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        player, action = next(p_a)
        print(f"Event {i}: Player {player} did action {action}")

    for i in range(10):
        player, action = next(p_a)
        event_list.append((player, action))
    print("Built list of 10 events: ", event_list)

    erase_gen = consume_event(event_list)
    for retire in erase_gen:
        print(f"Got event from list: {retire}")
        print(f"Remains in list: {event_list}")
