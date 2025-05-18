from fastapi import APIRouter, HTTPException
from app.core.kb_loader import load_kb
from app.core.resolver import resolve_property

router = APIRouter()
kb = load_kb()

@router.get("/")
def list_branches(city: str = None):
    branches = kb["branches"]
    if city:
        return [b for b in branches if b["address_info"]["city"].lower() == city.lower()]
    return branches

@router.get("/{property_id}")
def get_branch(property_id: str):
    resolved = resolve_property(property_id)
    
    for b in kb["branches"]:
        if b["property"] == resolved:
            return b
    raise HTTPException(404, "Branch not found")
