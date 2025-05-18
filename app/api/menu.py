from fastapi import APIRouter
from core.kb_loader import load_kb

router = APIRouter()
kb = load_kb()

@router.get("")
def get_menu():
    return kb["menu"]

def get_menu_data(menu_type: str = None):
    if menu_type == "veg":
        return {"veg": kb["menu"].get("veg", {})}
    elif menu_type == "nonveg" or menu_type == "non_veg":
        return {"non_veg": kb["menu"].get("non_veg", {})}
    else:
        return kb["menu"]
