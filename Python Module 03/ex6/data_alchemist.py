# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    data_alchemist.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/07 19:53:19 by azahino-          #+#    #+#             #
#    Updated: 2026/08/07 19:53:20 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import random



player_l = ['Al', "bob", "Carl", "Dyl", "En", "Greg", "jon", "kev", "Liam"]
cap_list = []
print(f"Initial list of players: {player_l}")
i = 0
while j >

while i < len(player_l):
    txt = player_l[i]
    if txt == txt.capitalize():
        cap_list.append(txt)
    i += 1
print(f"New list with all names capitalized: {cap_list}")