#!/usr/bin/env python3

import sys

from typing import IO


def to_print(text: str) -> None:
    print(f"Accessing file {sys.argv[1]}\n---")
    print(f"\n{text}")
    print(f"---\nFile {sys.argv[1]} closed.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        print(f"Accesing file: '{sys.argv[1]}'")
        try:
            file: IO[str] = open(sys.argv[1])
            text = file.read()
            to_print(text)
            file.close()
        except FileNotFoundError as error:
            print(f"Error opening file '{sys.argv[1]}': {error}\n")
        except PermissionError as error:
            print(f"Error opening file '{sys.argv[1]}': {error}\n")
