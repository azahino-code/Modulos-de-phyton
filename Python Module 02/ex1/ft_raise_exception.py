#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    else:
        return temp_int


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'.")
    try:
        temperature = input_temperature(temp_str)
        print(f"Temperature is now {temperature}°C.\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")
    test_temperature("25")
    test_temperature("abc")
    test_temperature("100")
    test_temperature("-100")
    print("All test completed - program didn't crash!")
