# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_ancient_text.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/20 20:57:04 by azahino-          #+#    #+#             #
#    Updated: 2026/08/20 20:57:05 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys

from typing import IO
# Similar a cuando importabamos genreator en ejercicios anteriores
# Este es un typehint, para objetos de entrada y salida.


def to_print(text: str) -> None:
    print(f"Accessing file {sys.argv[1]}\n---")
    print(f"\n{text}")
    print(f"---\nFile {sys.argv[1]} closed.")


print("=== Cyber Archives Recovery ===")
try:
    file: IO = open(sys.argv[1])
    text = file.read()
    to_print(text)
    file.close()
except FileNotFoundError as error:
    print(f"Error opening file {sys.argv[1]}: {error}\n")
except PermissionError as error:
    print(f"Error opening file {sys.argv[1]}: {error}\n")
