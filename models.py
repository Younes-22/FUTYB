from typing import Optional
from sqlmodel import SQLModel, Field

class Card(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    position: str
    nation: str
    league: str
    club: str
    age: int
    height: int
    weight: int
    overall: int
    pace: int
    shooting: int
    passing: int
    dribbling: int
    defending: int
    physical: int
    skill_moves: int
    weak_foot: int
    preferred_foot: str
    traits: str

    gk_diving: Optional[int] = Field(default=None)
    gk_handling: Optional[int] = Field(default=None)
    gk_kicking: Optional[int] = Field(default=None)
    gk_reflexes: Optional[int] = Field(default=None)
    gk_speed: Optional[int] = Field(default=None)
    gk_positioning: Optional[int] = Field(default=None)

    @property
    def is_goalkeeper(self) -> bool:
        return self.position == "GK"
