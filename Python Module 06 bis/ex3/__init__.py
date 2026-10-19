from .factory import (
    CreatureFactory,
    FireFactory,
    TransformationFactory
)
from .creatures import Creature
from .habilities import TransformCapability


__all__ = [
    "CreatureFactory",
    "FireFactory",
    "TransformationFactory",
    "Creature",
    "TransformCapability"
]
'''
Estructura: 
from {archivo de esta carpeta} import {funcion o clase deseada}
declararlo con un:
    - __all__ = ["{Nombre de la funcion importada}"]
'''