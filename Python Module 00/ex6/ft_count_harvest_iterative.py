# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/16 12:25:33 by azahino-          #+#    #+#             #
#    Updated: 2026/07/16 13:09:27 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative():
    h_time = int(input("Days until harvest: "))
    for i in range(h_time + 1):
        print("Day", i)
    print("Harvest time!")

# ft_count_harvest_iterative()
