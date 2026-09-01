# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    data_processor.py                                  :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/28 22:45:50 by azahino-          #+#    #+#             #
#    Updated: 2026/08/28 22:45:50 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #



from abc import ABC, abstractmethod

from typing import Any


class DataProcessor(ABC):
    def __init__(self):
        self.rank = 1
        self.value: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        ret = self.value[0]
        del self.value[0]
        return ret


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, int | float):
            return True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, int | float):
                    pass
                else:
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if isinstance(data, int | float):
            if self.validate(data):
                add = self.rank, str(data)
                self.value.append(add)
                self.rank += 1
            else:
                raise ValueError("Invalid data.")
        elif isinstance(data, list):
            for item in data:
                if self.validate(item):
                    add = self.rank, str(item)
                    self.value.append(add)
                    self.rank += 1
                else:
                    raise ValueError("Invalid data.")
        else:
            raise ValueError("Invalid data.")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, str):
                    pass
                else:
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if isinstance(data, str):
            if self.validate(data):
                add = self.rank, str(data)
                self.value.append(add)
                self.rank += 1
            else:
                raise ValueError("Invalid data.")
        elif isinstance(data, list):
            for item in data:
                if self.validate(item):
                    add = self.rank, str(item)
                    self.value.append(add)
                    self.rank += 1
                else:
                    raise ValueError("Invalid data.")
        else:
            raise ValueError("Invalid data.")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(key, str) and isinstance(value, str):
                    pass
                else:
                    return False
            return True
        elif isinstance(data, list):
            for obj in data:
                if self.validate(obj):
                    pass
                else:
                    return False
            return True
        else:
            return False
            

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if isinstance(data, dict):
            if self.validate(data):
                text = ""
                count = 1
                for key in data:
                    if count == 1:
                        text = data[key]
                        count += 1
                    else:
                        text = text + ": " + data[key]
                add = self.rank, text
                self.value.append(add)
                self.rank += 1
            else:
                raise ValueError("Invalid data.")
        elif isinstance(data, list):
            if self.validate(data):
                i = 0
                while i < len(data):
                    text = ""
                    count = 1
                    diccionary = data[i]
                    for key in diccionary:
                        if count == 1:
                            text = diccionary[key]
                            count += 1
                        else:
                            text = text + ": " + diccionary[key]
                    add = self.rank, text
                    self.value.append(add)
                    self.rank += 1
            else:
                raise ValueError("Invalid data.")
        else:
            raise ValueError("Invalid data.")
