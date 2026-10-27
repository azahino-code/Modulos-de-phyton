#!/usr/bin/env python3

import sys
from typing import IO


def to_print(text: str, file_name: str) -> None:
    print(f"\n{text}")
    print(f"---\nFile {file_name} closed.")


def text_to_write(write: str, in_text: str) -> str:
    lines: list[str] = in_text.splitlines()
    final_text = ""
    for line in lines:
        final_text = final_text + line + write + "\n"
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
        file: IO[str] | None = None
        try:
            print(f"Saving data to {f_name}")
            file = open(f_name, "w")
            file.write(mod_text)
            print(f"Data saved in file {f_name}")
        except OSError as error:
            message = "[STDERR] Error opening file"
            sys.stderr.write(message + f"'{f_name}': {error}\n")
            print("Data not saved.")
        finally:
            if file is not None:
                file.close()

if __name__ == "__main__":
    print("=== Cyber Archives Recovery & Preservation ===")
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
    else:
        file: IO[str] | None = None
        try:
            file = open(sys.argv[1])
            text = file.read()
            print(f"Accessing file {sys.argv[1]}\n---")
            to_print(text, sys.argv[1])
        except OSError as error:
            sys.stderr.write(
                f"[STDERR] Error opening file {sys.argv[1]}: {error}\n"
            )
            sys.exit(1)
        finally:
            if file is not None:
                file.close()
        
        print("\nTransform Data:\n---")

        mod_text = text_to_write("#", text)
        try:
            file = open(sys.argv[1], "w")
            file.write(mod_text)
        except OSError as error:
            sys.stderr.write(
                f"[STDERR] Error writing to file {sys.argv[1]}: {error}\n"
            )
            sys.exit(1)
        finally:
            if file is not None:
                file.close()
        try:
            file = open(sys.argv[1])
            to_print(file.read(), sys.argv[1])
        except OSError as error:
            sys.stderr.write(
                f"[STDERR] Error writing to file {sys.argv[1]}: {error}\n"
            )
            sys.exit(1)
        finally:
            if file is not None:
                file.close()
        copy_in_new(mod_text)
