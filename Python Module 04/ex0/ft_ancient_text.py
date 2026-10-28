#!/usr/bin/env python3

import sys
from typing import IO


def to_print(text: str) -> None:
    print(f"---\n\n{text}\n---")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        sys.exit(1)
    else:
        filename: str = sys.argv[1]
        print(
            "=== Cyber Archives Recovery ===\n"
            f"Accessing file: '{sys.argv[1]}'"
        )
        file: IO[str] | None = None
        try:
            file = open(filename, "r")
            text = file.read()
            to_print(text)
            print(f"File '{filename}' closed.")
        except OSError as error:
            print(f"Error opening file '{filename}': {error}\n")
            sys.exit(1)
        finally:
            if file is not None:
                file.close()
