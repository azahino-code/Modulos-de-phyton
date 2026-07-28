# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_command_quest.py                                :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/28 11:46:31 by azahino-          #+#    #+#             #
#    Updated: 2026/07/28 11:46:32 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys

def print_bucle(it: int, limit: int) -> None:
    if it < limit:
        print(f"Argument {it}: {sys.argv[it]}")
        print_bucle(it + 1, limit)
    else:
        pass


print("=== Command Quest ===")
print(f"Program name: {sys.argv[0]}")
if len(sys.argv) <= 1:
    print("No arguments provided!")
else:
    print(f"Arguments received: {len(sys.argv) - 1}")
    print_bucle(1, len(sys.argv))
print(f"Total argments {len(sys.argv)}\n")
