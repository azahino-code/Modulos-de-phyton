# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#    data_stream.py                                     :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#    By: azahino- <azahino-@student.42urduliz.com   +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#    Created: 2026/08/28 22:46:16 by azahino-          #+#    #+#             #
#    Updated: 2026/08/28 22:46:16 by azahino-         ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

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
    def __init__(self) -> None:
        super().__init__()
        self.name = "NumericProcessor"

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
        super().__init__()
        self.name = "TextProcessor"

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
        super().__init__()
        self.name = "LogProcessor"

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
        self.data = []

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
            if processed == False:
                remaining.append(data)
            if len(remaining) > 0:
                print(f"DataStream Error - Can't process element in stream: {remaining}")
                del(remaining)

    def print_processors_stats(self) -> None:
        print("== DataStream stadistics ==")
        if len(self.processors) == 0 and len(self.data) == 0:
            print("No processor found, no data")
        else:
            for p in self.processors:
                text1 = f"{p.name}: total {p.rank - 1}, remaining"
                print(f"{text1}  {len(p.value)} on processor")

print("=== Code Nexus - Data Stream ===\n")
numeric = NumericProcessor()
txt = TextProcessor()
log = LogProcessor()
data = DataStream()
print("Initialize Data Stream...")
data.print_processors_stats()

print("Registering Numeric Processor\n")

stream: list = (
    ['Hello world', [3.14, -1, 2.71], [{'log_level': 'WARNING',
    'log_message': 'Telnet access! Use ssh instead'},
    {'log_level': 'INFO',
      'log_message': 'User wil isconnected'}], 42, ['Hi', 'five']]
)

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
    "\nConsume some elements from the data processors: " \
    "Numeric 3, Text 2, Log 1"
)
numeric.output()
numeric.output()
numeric.output()
txt.output()
txt.output()
log.output()
data.print_processors_stats()