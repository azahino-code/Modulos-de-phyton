#!/usr/bin/env python3

def garden_operations(operation_numbers: int) -> None:
    if operation_numbers == 0:
        int("abc")
    elif operation_numbers == 1:
        10 / 0
    elif operation_numbers == 2:
        open("file.txt")
    elif operation_numbers == 3:
        "32456" + 11
    else:
        print("Operation completed successfully!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        try:
            print(f"Testing operation {i}")
            garden_operations(i)
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")
    print("\nAll error types tested succesafully!")


if __name__ == "__main__":
    test_error_types()
