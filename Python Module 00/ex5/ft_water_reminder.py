# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_water_reminder.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/16 12:21:39 by azahino-          #+#    #+#             #
#    Updated: 2026/07/16 13:09:19 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if (days <= 2):
        print("Plants are fine")
    else:
        print("Water the plants!")

# ft_water_reminder()
