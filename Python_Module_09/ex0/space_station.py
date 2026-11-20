from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, List, Dict

# instalar pydantic en la maquina virtual
# -> pip install -r requirements.txt

class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=50)
    power_level: float = Field(ge=0.0, le=100.0)
    oxigen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = datetime
    is_operative: bool = Field(default=True)
    notes: str | None = Field(default=None, min_length=1, max_length=200)


def print_station(s: SpaceStation) -> None:
    print(
        f"Station id: {s.station_id}",
        f"Name: {s.name}",
        f"Crew_sixe: {s.crew_size}",
        f"Power_level: {s.power_level}",
        f"Oxigen_level: {s.oxigen_level}",
        f"Last Maintenance: {s.last_maintenance}",
        f"Is operative?: {s.is_operative}",
        sep="\n"
	)
    if s.notes is not None:
        print(s.notes)


if __name__ == "__main__":
    space_station = SpaceStation(
        "SS-23",
        "Starfield",
        4,
        45.34,
        100.00,
        "2026/12/3"
	)
    print_station(space_station)

