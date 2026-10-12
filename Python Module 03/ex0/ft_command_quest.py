#!/usr/bin/env python3

import sys


def print_bucle(it: int, limit: int) -> None:
    if it < limit:
        print(f"Argument {it}: {sys.argv[it]}")
        print_bucle(it + 1, limit)
    else:
        pass


if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) <= 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(sys.argv) - 1}")
        print_bucle(1, len(sys.argv))
    print(f"Total argments {len(sys.argv)}")
