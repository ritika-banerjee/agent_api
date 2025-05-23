from fastapi import APIRouter, HTTPException
from app.models.val_num import Number
from app.core.kb_loader import load_kb


router = APIRouter()

@router.post("/validate-number")
def validate_number(req: Number):
    num = req.number
    
    if len(num) != 10 or not num.isdigit():
        raise HTTPException(status_code=400, detail="Not a valid number")
    
    return {
        "reply": "Thank you!"
    }