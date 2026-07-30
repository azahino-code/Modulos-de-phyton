# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_score_analytics.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/28 12:04:32 by azahino-          #+#    #+#             #
#    Updated: 2026/07/28 12:04:33 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys


def convert_int(index: int, argument) -> int:
    if index == len(argument):
        return 0
    try:
        argument[index] = int(argument[index])
        convert_int(index + 1, argument)
        return 0
    except ValueError as error:
        print(f"ValueError: {error}")
        convert_int(index + 1, argument)
        return 1


if len(sys.argv) <= 1:
    print("There aren't arguments. Please, introduce valid args.")
else:
    args = sys.argv[1:]
    print("=== Player Acore Analytics ===")
    error = convert_int(0, args)
    if error == 1:
        print(f"No scores provided. Usage: python3 {sys.argv}")
        sys.exit()
    scores: list[int] = sys.argv[1:]
    print(f"Score processed: {scores}")
    print(f"Total players: {len(sys.argv) - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
