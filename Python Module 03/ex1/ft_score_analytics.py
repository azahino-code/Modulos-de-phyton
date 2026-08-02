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


def convert_int(index: int, argument, scores, is_error) -> int:
    if index == len(argument):
        return is_error
    try:
        scores.append(int(argument[index]))
        is_error = convert_int(index + 1, argument, scores, is_error)
        return is_error
    except ValueError as error:
        print(f"ValueError: {error}")
        convert_int(index + 1, argument, scores, is_error)
        return 1


if len(sys.argv) <= 1:
    print("There aren't arguments. Please, intbuce valid args.")
else:
    args = sys.argv[1:]
    scores: list[int] = []
    print("=== Player Acore Analytics ===")
    error = convert_int(0, args, scores, 0)
    if error == 1:
        print(f"No scores provided. Usage: python3 {sys.argv}")
        sys.exit()
    print(f"Score processed: {scores}")
    print(f"Total players: {len(sys.argv) - 1}")
    print(f"Total score: {sum(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")
