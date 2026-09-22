# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    __init__.py                                        :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/11 23:20:37 by azahino-          #+#    #+#             #
#    Updated: 2026/09/11 23:20:43 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from .potions import strength_potion, healing_potion as heal

__all__ = [strength_potion, heal]
