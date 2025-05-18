from fastapi import APIRouter
from models.chat import ChatRequest
from core.faiss_index import search_faq
from core.kb_loader import load_kb
from core.resolver import resolve_property
from api.menu import get_menu_data

router = APIRouter()
kb = load_kb()

faq_keywords = [
    "halal",
    "jain",
    "drinks",
    "mocktails",
    "desserts",
    "menu",
    "alcohol",
    "alcoholic",
    "hookah",
    "pizza",
    "kulfi",
    "mutton",
    "fish",
    "prawns",
    "ice cream",
    "biryani",
    "outside drinks",
    "customize",
    "certificate",
    "proof",
    "takeaway",
    "delivery",
    "buffet"
]

@router.post("")
def chat(req: ChatRequest):
    msg = req.message.lower()

    if any(w in msg for w in faq_keywords):
        return search_faq(req.message)
    
    if "veg" in msg:
        return get_menu_data("veg")

    if "nonveg" in msg or "non veg" in msg or "non_veg" in msg:
        return get_menu_data("nonveg")

    if "menu" in msg:
        return get_menu_data()

    branch_key = resolve_property(msg)
    if branch_key:
        outlet = next((b for b in kb["branches"] if b["property"] == branch_key), None)
        return {
            "reply": f"You seem to be referring to {outlet['display_name']}. What would you like to do? (book/cancel/update)"
        }

    return {"reply": "I'm not sure what you're referring to. Can you clarify your intent?"}


        
    
    