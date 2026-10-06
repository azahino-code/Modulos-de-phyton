# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_garden_data.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: azahino- <azahino-@student.42urduliz.com>   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/07/17 11:30:54 by azahino-           #+#    #+#             #
#   Updated: 2026/10/06 18:37:51 by azahino-          ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

class Plant:
    def __init__(self, name, cm, days):
        self.name = name
        self.heigh = cm
        self.age = days

    def show(self) -> None:
        print(f"{self.name}: {self.heigh}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("rose", "25", "30")
    plant2 = Plant("Sunflower", "80", "45")
    plant3 = Plant("Cactus", "15", "120")
    print("=== Garden Plant Registry ===")
    plant1.show()
    plant2.show()
    plant3.show()

# self("rose", "25", "30").show() esto tambien funciona
