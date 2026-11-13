from pydantic import BaseModel, Field
from data_generator import SpaceStationGenerator, DataConfig
from dataclasses import dataclass, Field
from datetime import datetime

# instalar pydantic en la maquina virtual
# -> pip install -r requirements.txt

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=50)
    power_level: float = Field(ge=0.0, le=100.0)
    oxigen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime)
    is_operative: bool = Field(default=True)
    notes: str | None = Field(default=None, min_length=1, max_length=200)

if __name__ == "__main__":
    generator = SpaceStationGenerator(DataConfig())
    spaceship = SpaceStation(generator)
    print(SpaceStation)
