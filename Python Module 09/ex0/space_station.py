from pydantic import BaseModel, field


class SpaceStation(BaseModel):
    station_id: str = field(min_length=3, max_length=10)
    name: str = field(min_length=1, max_length=50)
    crew_size: int = field(ge=1, le=50)
    power_level: float = field(ge=0.0, le=100.0)
    oxigen_level: float = field(ge=0.0, le=100.0)
    last_maintenance: datatime = field(default_factory)
    is_operative: bool = field(default=True)
    notes: str | None = field(default=None, min_length=1, max_length=200)

print()