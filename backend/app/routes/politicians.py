from fastapi import APIRouter
from app.models.politician import Politician
import json
from pathlib import Path

router = APIRouter()

def load_politicians():
    path = Path("data/processed/politicians.json")
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Politician(**item) for item in data]
    else:
        return []

@router.get("/", response_model=list[Politician])
def get_politicians():
    return load_politicians()
