#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
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
        print(f"Caught input_temperature error: {error}")
    print("\nAll test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
