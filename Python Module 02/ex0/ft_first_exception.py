#!/usr/bin/env python3

def input_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int: int = int(temp_str)
        print(f"Temperature is now {temp_int}ºC\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    input_temperature("25")
    input_temperature("abc")
    print("\nAll test completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
