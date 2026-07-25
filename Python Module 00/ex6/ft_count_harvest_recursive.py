# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/16 12:32:25 by azahino-          #+#    #+#             #
#    Updated: 2026/07/18 22:16:12 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_recursive_count(i, n):
    if i == n:
        return print("Harvest time!")
    print("Day ", i)
    return (ft_recursive_count(i + 1, n))


def ft_count_harvest_recursive():
    h_days = int(input("Days until harvest: "))
    ft_recursive_count(0, h_days + 1)

# ft_count_harvest_recursive()
