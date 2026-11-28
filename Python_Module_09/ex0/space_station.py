from pydantic import BaseModel, Field
from datetime import datetime

# instalar pydantic en la maquina virtual
# -> pip install -r requirements.txt


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=50)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = datetime.now()
    is_operative: bool = Field(default=True)
    notes: str | None = Field(default=None, min_length=1, max_length=200)


def print_station(s: SpaceStation) -> None:
    print(
        f"ID: {s.station_id}",
        f"Name: {s.name}",
        f"Crew: {s.crew_size} people",
        f"Power: {s.power_level}",
        f"Oxygen: {s.oxygen_level}",
        f"Status: {s.is_operative}",
        sep="\n"
    )
    if s.notes is not None:
        print(s.notes)


if __name__ == "__main__":
    try:
        space_station = SpaceStation(
            station_id="SS-23",
            name="Starfield",
            crew_size=4,
            power_level=45.34,
            oxygen_level=100.00,
            last_maintenance="2026-12-03T10:30:00"
        )
    except ValueError as e:
        print (e) 
    print(
        "Space Station Data Validation",
        "========================================",
        "Valid station created:",
        sep="\n"
    )
    print_station(space_station)
    print(
        "\n========================================",
        "Expectes validation error:",
        sep="\n"
    )
    try:
        space_station = SpaceStation(
            station_id="SS-23",
            name="Starfield",
            crew_size=44,
            power_level=45.34,
            oxygen_level=100.00,
            last_maintenance="2026-12-03T10:30:00"
        )
    except ValueError as e:
        print(e)
