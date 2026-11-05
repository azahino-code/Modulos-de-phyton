from .factory import (
    CreatureFactory,
    FireFactory,
    TransformationFactory
)

__all__ = [
    "CreatureFactory",
    "FireFactory",
    "TransformationFactory"
]
'''
Estructura: 
from {archivo de esta carpeta} import {funcion o clase deseada}
declararlo con un:
    - __all__ = ["{Nombre de la funcion importada}"]
'''