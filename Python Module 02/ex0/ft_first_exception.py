# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_first_exception.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/26 14:53:43 by azahino-          #+#    #+#             #
#    Updated: 2026/07/26 14:53:44 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def input_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        print(f"Temperature is now {temp_int}ºC\n")
    except ValueError as error:
        print(error)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    input_temperature("25")
    input_temperature("abc")
    print("\nAll test completed - program didn't crash!")


test_temperature()
