from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    model_validator
)
from enum import Enum
from datetime import datetime
from typing import Self


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def ft_validator(self) -> Self:
        if not self.mission_id.startswith('M'):
            raise ValueError('Mission ID must start with "M"')
        if not any(
            mem.rank in (Rank.CAPTAIN, Rank.COMMANDER) for mem in self.crew
        ):
            raise ValueError('Must have at least one Commander or Captain')
        if self.duration_days > 365:
            experienced_members = 0
            for mem in self.crew:
                if mem.years_experience >= 5:
                    experienced_members += 1
            if experienced_members < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need "
                    "50% experienced crew (5+ years)"
                )
        if not all(mem.is_active for mem in self.crew):
            raise ValueError("All crew members must be active")
        return self


def print_mission(mission: SpaceMission) -> None:
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for mem in mission.crew:
        print(
            f"- {mem.name} ({mem.rank.value}) "
            f"- {mem.specialization}"
        )
    print("\n=========================================")


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=29,
                    specialization="Engineering",
                    years_experience=6
                )
            ]
        )
        print_mission(mission)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
    print("Expected validation error:")
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2024, 6, 15),
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.LIEUTENANT,
                    age=45,
                    specialization="Mission Command",
                    years_experience=20
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=10
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=29,
                    specialization="Engineering",
                    years_experience=6
                )
            ]
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
