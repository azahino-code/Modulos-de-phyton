# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_transmutation_1.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.co    +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/22 19:46:57 by azahino-          #+#    #+#             #
#    Updated: 2026/09/22 19:46:58 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from alchemy import transmutation

print(
    "=== Transmutation 1 ===\n"
    "Import transmutation module directly"
    f"Testing lead to gold: {transmutation.recipe.lead_to_gold()}"
)