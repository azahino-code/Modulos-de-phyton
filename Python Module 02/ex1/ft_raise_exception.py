#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    else:
        return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    try:
        print("Input data is '25'")
        temp_int = input_temperature("25")
        print(f"Temperature is now {temp_int}ºC\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    try:
        print("Input data is 'abc'")
        temp_int = input_temperature("abc")
        print(f"Temperature is now {temp_int}ºC\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")
    try:
        print("Input data is '100'")
        temp_int = input_temperature("100")
        print(f"Temperature is now {temp_int}ºC\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")
    try:
        print("Input data is '-50'")
        temp_int = input_temperature("-50")
        print(f"Temperature is now {temp_int}ºC\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")
    print("All test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
