from fastapi import APIRouter, Query
from core.faiss_index import search_faq

router = APIRouter()

@router.get("")
def faq(query: str = Query(..., description="FAQ question")):
    return search_faq(query)
