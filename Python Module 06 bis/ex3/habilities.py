from abc import ABC, abstractmethod


class TransformCapability(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
