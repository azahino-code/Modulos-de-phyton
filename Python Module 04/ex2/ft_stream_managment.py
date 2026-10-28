#!/usr/bin/env python3

import sys
from typing import IO


def text_to_write(write: str, in_text: str) -> str:
    lines: list[str] = in_text.splitlines()
    final_text = ""
    for line in lines:
        final_text = final_text + line + write + "\n"
    return final_text


def my_input(txt: str) -> str:
    sys.stdout.write(txt)
    line = sys.stdin.readline()
    if line.endswith("\n"):
        line = line[:-1]
    return line


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
            sys.stderr.write(
                f"[STDERR] Error opening file '{f_name}': {error}\n"
            )
            print("Data not saved.")
            sys.exit(1)
        finally:
            if file is not None:
                file.close()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        sys.exit(1)
    else:
        file_name = sys.argv[1]
        print("=== Cyber Archives Recovery ===\n")
        file: IO[str] | None = None
        try:
            file = open(file_name)
            text = file.read()
            print(f"Accessing file {file_name}\n---")
            print(text)

        except OSError as error:
            sys.stderr.write(
                f"[STDERR] Error opening file {file_name}: {error}\n"
            )
            sys.exit(1)
        finally:
            if file is not None:
                file.close()
                print(f"---\nFile {file_name} closed.")

        print("\nTransform Data:\n---")

        mod_text = text_to_write("#", text)
        file = None
        try:
            file = open(file_name, "w")
            file.write(mod_text)
        except OSError as error:
            sys.stderr.write(
                f"[STDERR] Error writing to file {file_name}: {error}\n"
            )
            sys.exit(1)
        finally:
            if file is not None:
                file.close()
        file = None
        try:
            file = open(file_name)
            print(file.read())
        except OSError as error:
            sys.stderr.write(
                f"[STDERR] Error opening file {file_name}: {error}\n"
            )
            sys.exit(1)
        finally:
            if file is not None:
                file.close()
                print(f"---\nFile {file_name} closed.")
        copy_in_new(mod_text)
