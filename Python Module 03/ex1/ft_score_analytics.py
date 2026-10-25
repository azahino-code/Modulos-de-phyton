#!/usr/bin/env python3

import sys


def convert_int(values: list[str]) -> list[int]:
    scores: list[int] = []
    for value in values:
        try:
            scores.append(int(value))
        except ValueError:
            print(f"Invalid parameter: '{value}'")
    return scores


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(
            "No scores provided. Usage: python3"
            f" {sys.argv[0]} <score1> <score2> ..."
        )
    else:
        args: list[str] = sys.argv[1:]
        print("=== Player Score Analytics ===")
        scores: list[int] = convert_int(args)
        if len(scores) == 0:
            print(f"No valid scores provided. Usage: python3 {sys.argv[0]}")
            sys.exit()
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
