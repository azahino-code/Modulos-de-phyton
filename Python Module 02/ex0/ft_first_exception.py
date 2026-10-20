#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str) 


def test_temperature() -> None:
    try:
        print(f"Input data is '25'")
        temp_int = input_temperature("25")
        print(f"Temperature is now {temp_int}ºC\n")
        print(f"Input data is 'abc'")
        temp_int = input_temperature("abc")
        print(f"Temperature is now {temp_int}ºC\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    test_temperature()
    print("\nAll test completed - program didn't crash!")
