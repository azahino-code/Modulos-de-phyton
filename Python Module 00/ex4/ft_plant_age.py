# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_plant_age.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: azahino- <azahino-@student.42urduliz.com>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/16 12:16:54 by azahino-           #+#    #+#             #
#   Updated: 2026/10/06 16:29:22 by azahino-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_plant_age() -> None:
    plant_age = int(input("Enter plan age in days: "))
    if (plant_age <= 60):
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")

# ft_plant_age()
