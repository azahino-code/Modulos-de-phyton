#!/usr/bin/env python3

from abc import ABC, abstractmethod

from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.rank = 0
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
        try:
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
                        raise ValueError("Improper numeric data")
            else:
                raise ValueError("Improper numeric data")
        except ValueError as error:
            print(f"Get exception: {error}")


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
        try:
            if isinstance(data, str):
                if self.validate(data):
                    add = self.rank, str(data)
                    self.value.append(add)
                    self.rank += 1
                else:
                    raise ValueError("Improper text data")
            elif isinstance(data, list):
                for item in data:
                    if self.validate(item):
                        add = self.rank, str(item)
                        self.value.append(add)
                        self.rank += 1
                    else:
                        raise ValueError("Improper text data")
            else:
                raise ValueError("Improper text data")
        except ValueError as error:
            print(f"Get exception: {error}")


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
        try:
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
                    for diccionary in data:
                        text = ""
                        count = 1
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
        except ValueError as error:
            print(f"Get exception: {error}")


if __name__ == "__main__":
    print(
        "=== Code Nexus - Data Processor ===\n\n"
        "Testing Numeric Processor..."
    )
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    print(
        f"Trying to validate input '42': {numeric.validate(42)}\n"
        f"Trying to validate input 'Hello': {numeric.validate("Hello")}\n"
        f"Test invalid ingestion of string 'foo' without prior validation:"
    )
    numeric.ingest("foo")
    num: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num}")
    numeric.ingest(num)
    print("Extracting 3 values...")
    for i in range(3):
        to_p = numeric.output()
        print(f"Numeric value {to_p[0]}: {to_p[1]}")

    txt = ['Hello', 'Nexus', 'World']
    print(
        "\nTesting Text Processor...\n"
        f"Trying to validate input '42': {text.validate(42)}\n"
        f"Processing data: {txt}"
    )
    text.ingest(txt)
    print("Extracting 1 value...")
    for i in range(1):
        to_p = text.output()
        print(f"Text value {to_p[0]}: {to_p[1]}")
    print()
    logg = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(
        "Texting Log Proccesor...\n"
        f"Trying to validate input 'Hello': {log.validate("Hello")}\n"
        f"Processing data: {logg}"
    )
    log.ingest(logg)
    print("Extracting 2 values...")
    for i in range(2):
        to_p = log.output()
        print(f"Log value {to_p[0]}: {to_p[1]}")
