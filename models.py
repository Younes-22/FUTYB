from typing import Optional
from sqlmodel import SQLModel, Field

defending: Optional[float] = Field(default=None)

class Card(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    name: str
    position: str
    nationality: str
    league: str
    club: str

    age: Optional[int] = Field(default=None)
    height: Optional[int] = Field(default=None)
    weight: Optional[int] = Field(default=None)
    overall: Optional[int] = Field(default=None)
    pace: Optional[int] = Field(default=None)
    shooting: Optional[int] = Field(default=None)
    passing: Optional[int] = Field(default=None)
    dribbling: Optional[int] = Field(default=None)
    defending: Optional[int] = Field(default=None)
    physical: Optional[int] = Field(default=None)
    skill_moves: Optional[int] = Field(default=None)
    weak_foot: Optional[int] = Field(default=None)
    preferred_foot: Optional[str] = Field(default=None)
    traits: Optional[str] = Field(default=None)

    gk_diving: Optional[int] = Field(default=None)
    gk_handling: Optional[int] = Field(default=None)
    gk_kicking: Optional[int] = Field(default=None)
    gk_reflexes: Optional[int] = Field(default=None)
    gk_speed: Optional[int] = Field(default=None)
    gk_positioning: Optional[int] = Field(default=None)

    @property
    def is_goalkeeper(self) -> bool:
        return self.position == "GK"
