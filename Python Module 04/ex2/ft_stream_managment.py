#!usr/bin/env python3

import sys

from typing import IO


def acces_to_file(f_name: str, mode: str = "r") -> IO[str]:
    try:
        file: IO[str] = open(f_name, mode)
        return file
    except FileNotFoundError as error:
        sys.stderr.write(f"[STDERR] Error opening file {f_name}: {error}\n")
        sys.exit()
    except PermissionError as error:
        sys.stderr.write(f"[STDERR] Error opening file {f_name}: {error}\n")
        sys.exit()


def to_print(text: str, file_name: str) -> None:
    print(f"Accessing file {file_name}\n---")
    print(f"\n{text}")
    print(f"---\nFile {file_name} closed.")


def text_to_write(write: str, in_text: str) -> str:
    final_text: str = ""
    for character in in_text:
        if character != "\n":
            final_text = final_text + character
        else:
            final_text = final_text + write + character
    final_text = final_text + write
    return final_text


def my_input(txt: str) -> str:
    sys.stdout.write(txt)
    line = sys.stdin.readline()
    final_line = ""
    i = 0
    for c in line:
        if i <= len(line) - 2:
            final_line = final_line + c
            i += 1
    return final_line


def copy_in_new(mod_text: str) -> None:
    f_name = my_input("Enter new file name (or empty): ")
    sys.stdout.write("\n")
    if f_name == "":
        print("Not saving data")
    else:
        try:
            file = open(f_name)
            txt = file.read()
            file.close()
            if txt == "":
                print(f"Saving data to {f_name}")
                file = open(f_name, "w")
                file.write(mod_text)
                file.close()
                print(f"Data saved in file {f_name}")
            else:
                print(f"{f_name} is filled, try again.\n")
                copy_in_new(mod_text)
        except FileNotFoundError as error:
            message = "[STDERR] Error opening file"
            sys.stderr.write(message + f"'{f_name}': {error}\n")
            print("Data not saved.")
        except PermissionError as error:
            message = "[STDERR] Error opening file"
            sys.stderr.write(message + f"'{f_name}': {error}\n")
            print("Data not saved.")


if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) < 2:
        print("Usage: ft_stream_management.py <file>")
    else:
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

        copy_in_new(mod_text)
