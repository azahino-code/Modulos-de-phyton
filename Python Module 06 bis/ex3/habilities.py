from abc import ABC
from .creatures import Creature


class TransformCapability(ABC):
    def __init__(self):
        pass

    @classmethod
    def transform(cls) -> str:
        pass

    @classmethod
    def revert(cls) -> str:
        pass
