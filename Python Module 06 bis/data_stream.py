from abc import ABC, abstractmethod

from typing import Any


class DataProcessor(ABC):
    def __init__(self, name: str):
        self.rank = 0
        self.name = name
        self.value: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if len(self.value) <= 0:
            raise IndexError("No valid data.")
        else:
            ret = self.value[0]
            del self.value[0]
            return ret


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("NumericProcessor")

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
                raise ValueError("Improper numeric data")
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


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("TextProcessor")

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


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("LogProcessor")

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
                raise ValueError("Improper log data")
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
                raise ValueError("Improper log data")
        else:
            raise ValueError("Improper log data")


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.data: list[Any] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        self.data = stream
        for data in stream:
            processed = False
            remaining: list[Any] = []
            for p in self.processors:
                if p.validate(data):
                    try:
                        p.ingest(data)
                        processed = True
                        break
                    except ValueError as e:
                        print(f"An error occurred: {e}")
            if processed is False:
                remaining.append(data)
            if len(remaining) > 0:
                text = "DataStream Error - Can't process"
                print(f"{text} element in stream: ", end="")
                for i, r in enumerate(remaining):
                    if len(remaining) - 1 == i:
                        print(r)
                    else:
                        print(f"{r}, ", end="")
                del (remaining)

    def print_processors_stats(self) -> None:
        print("== DataStream stadistics ==")
        if len(self.processors) == 0:
            print("No processor found, no data")
        elif len(self.data) == 0:
            print("There is not data to process")
        else:
            for p in self.processors:
                print(
                    f"{p.name}: total {p.rank} items processed,"
                    f" remaining {len(p.value)} on processor"
                )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    numeric = NumericProcessor()
    txt = TextProcessor()
    log = LogProcessor()
    data = DataStream()
    print("Initialize Data Stream...")
    data.print_processors_stats()

    print("\nRegistering Numeric Processor\n")

    stream: list[Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [
            {
                'log_level': 'WARNING',
                'log_message': 'Telnet access! Use ssh instead'
            },
            {
                'log_level': 'INFO',
                'log_message': 'User will disconnected'
            }
        ],
        42,
        ['Hi', 'five']
    ]

    data.register_processor(numeric)

    print(f"Send first batch of data on stream: {stream}")
    data.process_stream(stream)
    data.print_processors_stats()

    print("\nRegistering other data processors")
    data.register_processor(txt)
    data.register_processor(log)

    print("Send the same batch again")
    data.process_stream(stream)
    data.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for i in range(3):
        try:
            numeric.output()
        except IndexError as e:
            print(f"{e}")
    for i in range(2):
        try:
            txt.output()
        except IndexError as e:
            print(e)
    for i in range(1):
        try:
            log.output()
        except IndexError as e:
            print(e)
    data.print_processors_stats()
