# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_inventory_system.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/02 14:30:28 by azahino-          #+#    #+#             #
#    Updated: 2026/08/02 14:30:29 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import sys


class Error(Exception):
    pass


listerine = sys.argv[1:]
bag: dict = {}
i: int = 0
try:
    while i < len(listerine):
        temp = listerine[i].split(":")
        if len(temp) != 2:
            raise Error(f"invalid parameter '{listerine[i]}'")
        if temp[0] in bag:
            print(f"Redundant item {temp[0]} - discarding")
        else:
            bag[temp[0]] = int(temp[1])
        i += 1
except Error as error:
    print(f"Error - {error}")
    sys.exit()
except ValueError as error:
    print(f"Quantity error for 'key': {error}")
    sys.exit()


print("=== Inventory System Analysis ===")
keys = list(bag.keys())
values = list(bag.values())
total = sum(bag.values())
print(f"Got inventory: {bag}")
print(f"Item list: {keys}")
print(f"Total quantity of the {len(bag.keys())} items: {total}")
i = 0
maxi = 0
mini = 2147483647
while i < len(keys):
    print(f"Item {keys[i]} represents {round((values[i]/total)*100, 1)}")
    if mini > values[i]:
        mini = values[i]
        min_q = [keys[i], values[i]]
    if maxi < values[i]:
        maxi = values[i]
        maxi_q = [keys[i], values[i]]
    i += 1
print(f"Item most abundant is: {maxi_q[0]} with quantity {maxi_q[1]}")
print(f"Item most abundant is: {min_q[0]} with quantity {min_q[1]}")
bag.update({"Magical_item": 1})
print(f"Inventori updated: {bag}")
