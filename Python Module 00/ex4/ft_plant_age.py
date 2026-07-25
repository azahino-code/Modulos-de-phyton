# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_plant_age.py                                    :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/16 12:16:54 by azahino-          #+#    #+#             #
#    Updated: 2026/07/16 13:09:15 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

# los if funcionan casi como los de C pero hay que ponerles :

def ft_plant_age():
    plant_age = int(input("Enter plan age in days: "))
    if (plant_age <= 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")

# ft_plant_age()
