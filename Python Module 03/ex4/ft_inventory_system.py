#!/usr/bin/env python3

import sys


class Error(Exception):
    pass


listerine = sys.argv[1:]
bag: dict[str, int] = {}

for object in listerine:
    try:
        temp = object.split(":")
        if len(temp) != 2:
            raise Error(f"invalid parameter '{object}'")
        if temp[0] in bag:
            print(f"Redundant item '{temp[0]}' - discarding")
        else:
            bag[temp[0]] = int(temp[1])
    except Error as error:
        print(f"Error - {error}")
        continue
    except ValueError as error:
        print(f"Quantity error for {temp[0]}: {error}")
        continue


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    try:
        if len(bag) == 0:
            raise Error("Inventory is empty")
        keys = list(bag.keys())
        values = list(bag.values())
        total = sum(bag.values())
        if total == 0:
            raise Error("Inventory is empty")
        print(f"Got inventory: {bag}")
        print(f"Item list: {keys}")
        print(f"Total quantity of the {len(bag.keys())} items: {total}")
        i = 0
        maxi = values[i]
        mini = values[i]
        min_q = [keys[i], values[i]]
        maxi_q = [keys[i], values[i]]
        while i < len(keys):
            print(
                f"Item {keys[i]} represents"
                f"{round((values[i] / total) * 100, 1)}%"
            )
            if mini > values[i]:
                mini = values[i]
                min_q = [keys[i], values[i]]
            if maxi < values[i]:
                maxi = values[i]
                maxi_q = [keys[i], values[i]]
            i += 1
        print(f"Item most abundant: {maxi_q[0]} with quantity {maxi_q[1]}")
        print(f"Item least abundant: {min_q[0]} with quantity {min_q[1]}")
        bag.update({"magic_item": 1})
        print(f"Updated inventory: {bag}")
    except Error as error:
        print(f"Error: {error}")
