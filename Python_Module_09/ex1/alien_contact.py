from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime
from enum import Enum
from typing import Self


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field(default_factory=datetime.now)
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def ft_validator(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "ID must start with 'AC'"
            )
        if not self.is_verified:
            raise ValueError("Must be verified.")
        if self.contact_type is ContactType.TELEPATHIC:
            if self.witness_count < 3:
                raise ValueError(
                    "Telepathic contact requires at least 3 witnesses"
                )
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError(
                    "Strong signals (> 7.0) should include received messages"
                )
        return self


def print_contact(a: AlienContact) -> None:
    print(
        "Alien Contact Log Validation",
        "=====================================",
        "Valid contact report:",
        f"ID: {a.contact_id}",
        f"Type: {a.contact_type}",
        f"Location: {a.location}",
        f"Signal: {a.signal_strength}/10",
        f"Duration: {a.duration_minutes} minutes",
        f"Witnesses: {a.witness_count}",
        f"Is verified?: {a.is_verified}",
        sep="\n"
    )
    if a.message_received is not None:
        print(a.message_received)
    print("\n=====================================")


if __name__ == "__main__":
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            location="Area 51, Nevada",
            contact_type=ContactType.VISUAL,
            signal_strength=8.5,
            duration_minutes=225,
            witness_count=52,
            is_verified=True
        )
        print_contact(contact)
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])
    print("Expected validation error:")
    try:
        contact = AlienContact(
            contact_id="AC_2024_001",
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=6.7,
            duration_minutes=225,
            witness_count=2,
            is_verified=True
        )
        print_contact(contact)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
