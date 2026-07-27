# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_different_errors.py                             :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/27 08:37:39 by azahino-          #+#    #+#             #
#    Updated: 2026/07/27 08:37:40 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def garden_operations(operation_numbers: int) -> None:
    try:
        if operation_numbers == 0:
            int("abc")
        elif operation_numbers == 1:
            10/0
        elif operation_numbers == 2:
            open("file.txt")
        elif operation_numbers == 3:
            "32456" + 11
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")


def test_error_types() -> None:
    print("Testing operation 0...")
    garden_operations(0)
    print("Testing operation 1...")
    garden_operations(1)
    print("Testing operation 2...")
    garden_operations(2)
    print("Testing operation 3...")
    garden_operations(3)
    print("\nAll error types tested succesafully!")


print(" === Garden Error Types Demo ===")
test_error_types()
