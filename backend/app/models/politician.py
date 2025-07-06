from pydantic import BaseModel
from typing import List

class Politician(BaseModel):
    id: int
    name: str
    party: str
    birth_year: int
    city: str
    topics: List[str]
    bio: str
    sentiment: str
    leaning: str