# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_archive_creation.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/20 22:12:41 by azahino-          #+#    #+#             #
#    Updated: 2026/08/20 22:12:42 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys

from typing import IO


def to_print(text: str) -> None:
    print(f"Accessing file {sys.argv[1]}\n---")
    print(f"\n{text}")
    print(f"---\nFile {sys.argv[1]} closed.")


print("=== Cyber Archives Recovery ===")
try:
    file: IO = open(sys.argv[1])
except FileNotFoundError as error:
    print(f"Error opening file {sys.argv[1]}: {error}\n")
except PermissionError as error:
    print(f"Error opening file {sys.argv[1]}: {error}\n")

text = file.read()
to_print(text)
file.close()

print("Transform Data:\n---")
file = open(sys.argv[1], "w")
final_text: str = ""
for character in text:
    if character != "\n":
        final_text = final_text + character
    else:
        final_text = final_text + "#" + character
final_text = final_text + "#"
file.write(final_text)
file.close()
file = open(sys.argv[1])
text = file.read()
to_print(text)
file.close()

f_name = input("Enter new file name (or empty): ")
if f_name == "":
    print("Not saving data")
else:
    file = open(f_name, "x")
    file.close()
    print(f"Saving data to {f_name}")
    file = open(f_name, "w")
    file.write(final_text)
    file.close()
    print(f"Data saved in file {f_name}")
