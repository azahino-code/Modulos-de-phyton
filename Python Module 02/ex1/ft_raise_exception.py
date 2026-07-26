# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_raise_exception.py                              :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/07/26 16:11:43 by azahino-          #+#    #+#             #
#    Updated: 2026/07/26 16:11:44 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def input_temperature(temp_str: str) -> int:
    temp_int = int(temp_str)
    if temp_int < 0:
        raise ValueError(f"{temp_int}ºC is too cold for plants (min 0ºC)")
    elif temp_int > 40:
        raise ValueError(f"{temp_int}ºC is too hot for plants (max 40ºC)")
    else:
        return temp_int


def test_temperature(temp_str: str) -> None:
    print(f"Input data is '{temp_str}'.")
    try:
        temperature = input_temperature(temp_str)
        print(f"Temperature is now {temperature}ºC.\n")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}\n")

print("=== Garden Temperature Checker ===\n")
test_temperature("100")
test_temperature("-50")
test_temperature("38")
test_temperature("3ewfdv")
print("All test completed - program didn't crash!")
