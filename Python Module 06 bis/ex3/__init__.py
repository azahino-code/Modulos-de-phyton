from .factory import (
    CreatureFactory,
    FireFactory,
    TransformationFactory
)
from .creatures import Creature


__all__ = [
    "CreatureFactory",
    "FireFactory",
    "TransformationFactory",
    "Creature"
]
'''
Estructura: 
from {archivo de esta carpeta} import {funcion o clase deseada}
declararlo con un:
    - __all__ = ["{Nombre de la funcion importada}"]
'''