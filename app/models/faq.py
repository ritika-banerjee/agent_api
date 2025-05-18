from pydantic import BaseModel

class FAQResponse(BaseModel):
    answer: str

