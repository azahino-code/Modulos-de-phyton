# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_seed_inventory.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/16 12:51:14 by azahino-          #+#    #+#             #
#    Updated: 2026/07/16 13:09:42 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} square meters")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    else:
        print("Unknown unit type")

# ft_seed_inventory("tomato", 15, "packets")
# ft_seed_inventory("carrot", 8, "grams")
# ft_seed_inventory("lettuce", 12, "area")
# ft_seed_inventory("lettuce", 12, "rope")
