#!/usr/bin/env python3

import sys

from typing import IO


def acces_to_file(file_name: str, mode: str = "r") -> IO[str]:
    try:
        file: IO[str] = open(file_name, mode)
        return file
    except FileNotFoundError as error:
        print(f"[STDERR] Error opening file {file_name}: {error}\n")
        sys.exit()
    except PermissionError as error:
        print(f"[STDERR] Error opening file {file_name}: {error}\n")
        sys.exit()


def to_print(text: str, file_name: str) -> None:
    print(f"Accessing file {file_name}\n---")
    print(f"\n{text}\n")
    print(f"---\nFile {file_name} closed.\n")


def text_to_write(write: str, in_text: str) -> str:
    final_text: str = ""
    for character in in_text:
        if character != "\n":
            final_text = final_text + character
        else:
            final_text = final_text + write + character
    final_text = final_text + write
    return final_text


if __name__ == "__main__":
    print("=== Cyber Archives Recovery ===")
    file = acces_to_file(sys.argv[1])
    text = file.read()
    file.close()
    to_print(text, sys.argv[1])

    print("\nTransform Data:\n---")

    mod_text = text_to_write("#", text)
    file = acces_to_file(sys.argv[1], "w")
    file.write(mod_text)
    file.close()
    file = acces_to_file(sys.argv[1])
    to_print(file.read(), sys.argv[1])
    file.close()

    f_name = input("Enter new file name (or empty): ")
    if f_name == "":
        print("Not saving data")
    else:
        file = acces_to_file(f_name, "x")
        file.close()
        print(f"Saving data to {f_name}")
        file = acces_to_file(f_name, "w")
        file.write(mod_text)
        file.close()
        print(f"Data saved in file {f_name}")
