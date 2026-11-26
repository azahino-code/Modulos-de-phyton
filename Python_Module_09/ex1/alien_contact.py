from pydantic import BaseModel, model_validator, Field
from datetime import datetime
from enum import Enum
from typing import Self


class ContactType(Enum):
    RADIO="radio"
    VISUAL="visual"
    PHYSICAL="physical"
    TELEPATHIC="telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: Enum = ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def ft_validator(self) -> Self:
        if not "AC" in self.contact_id[:1]:
            raise ValueError(
                f"ID start with {self.contact_id[:1]} instead of 'AC'"
            )
        if not self.is_verified:
            raise ValueError("Must be verified.")
        if self.contact_type is ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError(
                    "Strong signals (> 7.0) should include received messages"
                )
        return Self


def print_station(a: AlienContact) -> None:
    print(
        f"Station id: {a.station_id}",
        f"Name: {a.name}",
        f"Crew_sixe: {a.crew_size}",
        f"Power_level: {a.power_level}",
        f"Oxigen_level: {a.oxigen_level}",
        f"Last Maintenance: {a.last_maintenance}",
        f"Is operative?: {a.is_operative}",
        sep="\n"
	)
    if a.notes is not None:
        print(a.notes)

if __name__ == "__main__":
    contact = AlienContact(
        contact_id = "AC_2024_001",
        location = "Area 51, Nevada",
        contact_type = ContactType.VISUAL,
        signal_strength = 6.7,
        duration_minutes = 225,
        witness_count = 52,
        is_verified = True
    )

    

