#!/usr/bin/env python3

import sys


def convert_int(
    index: int, argument: list[str],
    scores: list[int], is_error: int
) -> int:
    if index == len(argument):
        return is_error
    try:
        scores.append(int(argument[index]))
        is_error = convert_int(index + 1, argument, scores, is_error)
        return is_error
    except ValueError as error:
        print(f"ValueError: {error}")
        convert_int(index + 1, argument, scores, is_error)
        return 1


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print(
            "No scores provided. Usage: python3"
            " ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        args: list[str] = sys.argv[1:]
        scores: list[int] = []
        print("=== Player Acore Analytics ===")
        error = convert_int(0, args, scores, 0)
        if error == 1:
            print(f"No scores provided. Usage: python3 {sys.argv}")
            sys.exit()
        print(f"Score processed: {scores}")
        print(f"Total players: {len(sys.argv) - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
