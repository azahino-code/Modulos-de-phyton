# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    data_pipeline.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/09/07 23:28:19 by azahino-          #+#    #+#             #
#    Updated: 2026/09/07 23:28:19 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod

from typing import Any, Protocol


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...

class CsvManual():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        for tupla in data:
            print(f"{tupla[0]}, {tupla[1]}")


class JsonManual():
    def process_output(self, data: list[tuple[int, str]]) -> None:
        for tupla in data:
            print(f'{{"rank": {tupla[0]}, "data": "{tupla[1]}"}}')


class DataProcessor(ABC):
    def __init__(self, name: str):
        self.rank = 1
        self.name = name
        self.value: list[tuple[int, str]] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def get_data(self) -> list[tuple[int, str]]:
        return self.value

    def output(self) -> tuple[int, str]:
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


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.data: list[Any] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        self.data = stream
        for data in stream:
            remaining: list[Any] = []
            processed = False
            for p in self.processors:
                if p.validate(data):
                    p.ingest(data)
                    processed = True
                    break
            if processed is False:
                remaining.append(data)
            if len(remaining) > 0:
                text = "DataStream Error - Can't process"
                print(f"{text} element in stream: {remaining}")
                del (remaining)


    def print_processors_stats(self) -> None:
        print("== DataStream stadistics ==")
        if len(self.processors) == 0 and len(self.data) == 0:
            print("No processor found, no data")
        else:
            for p in self.processors:
                text1 = f"{p.name}: total {p.rank - 1}, remaining"
                print(f"{text1}  {len(p.value)} on processor")


    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        lister: list[tuple[int, str]] = []
        for p in self.processors:
            index = nb
            if len(p.value) > 0:
                if index > len(p.value):
                    index = len(p.value)
                for i in range(index):
                    lister.append(p.output())
        plugin.process_output(lister)


numeric = NumericProcessor()
txt = TextProcessor()
log = LogProcessor()
data = DataStream()
json = JsonManual()
csv = CsvManual()

print("=== Code Nexus - Data Pipeline ===")
print("\nInitialize Data Stream...\n")
data.print_processors_stats()

print("Registering Processors")
data.register_processor(numeric)
data.register_processor(txt)
data.register_processor(log)

stream: list = [
    'Hello world',
    [3.14, -1, 2.71],
    [
        {'log_level': 'WARNING',
         'log_message': 'Telnet access! Use ssh instead'},
        {'log_level': 'INFO',
         'log_message': 'User wil isconnected'}
    ],
    42,
    ['Hi', 'five']
]
print("Send first batch of data on stream: {stream}\n")
data.process_stream(stream)
data.print_processors_stats()

print("send 3 processed data from each processor to a CSV plugin:")
print("CSV Output:")
data.output_pipeline(3, csv)
data.print_processors_stats()

stream = [
    21,
    [
        'I love IA',
        'LLMs are wonderful',
        'Stay healthy'
    ],
    [
        {'log_level': 'ERROR', 'log_message': '500 server crash'},
        {'log_level': 'NOTICE', 'log_message': 'Certificate expires in 10 days'}
    ],
    [32, 42, 64, 84, 128, 168],
    'World hello'
]

print(f"Send another batch of data {stream}\n")
data.process_stream(stream)
data.print_processors_stats()
print("Send 5 processed data from each processor to a JSON plugin:")
print("JSON Output")
data.output_pipeline(5, json)
data.print_processors_stats()
