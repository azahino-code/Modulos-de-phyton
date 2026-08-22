# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    data_processor.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/22 12:57:08 by azahino-          #+#    #+#             #
#    Updated: 2026/08/22 12:57:09 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod

from typing import Any

class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

#   @standarmethod
    def output(self) -> tuple[int, str]:



class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, int)

class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str)