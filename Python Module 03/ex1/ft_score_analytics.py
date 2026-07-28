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

try:
    scores = [sys.argv]
    print("=== Player Acore Analytics ===")
    print(f"Score processed: {scores}")
    print(f"Total players: {len(sys.argv) - 1}")
    print(f"Total score: {sum(sys.argv)}")
    print(f"High score: {max(sys.argv)}")
    print(f"Low score: {min(sys.argv)}")
    print(f"Score range: {max(sys.argv) - min(sys.argv)}")
except:
    print(f"")