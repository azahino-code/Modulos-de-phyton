# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    ft_vault_security.py                               :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/22 12:20:50 by azahino-          #+#    #+#             #
#    Updated: 2026/08/22 12:20:51 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

def secure_archive(m_filename: str, mode: str, cont: str) -> tuple[bool, str]:
    try:
        if mode == "read":
            with open(m_filename, "r") as file:
                text = file.read()
                return True, text
        elif mode == "write":
            with open(m_filename, "w") as file:
                file.write(cont)
                return True, "Content succesfully written to file"
        else:
            return False, "Incorrect 'mode', try again."
    except FileNotFoundError as error:
        return False, str(error)
    except PermissionError as error:
        return False, str(error)
