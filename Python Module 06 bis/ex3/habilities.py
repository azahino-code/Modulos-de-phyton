from abc import ABC
from .creatures import Creature


class HealCapability(ABC):
    def __init__(self):
        pass

    def heal(self, tarjet: Creature) -> None:
        if tarjet.evolved == False:
            return f"{self.name} heals itself for a small amount"
        else:
            return f"{self.name} heals itself and others for a large amount"
        

class TransformCapability(ABC):
    def __init__(self):
        pass

    @classmethod
    def transform(self) -> str:
        pass

    @classmethod
    def revert(self) -> str:
        pass
