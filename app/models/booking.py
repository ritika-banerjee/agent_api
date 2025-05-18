from pydantic import BaseModel

class BookingRequest(BaseModel):
    name: str
    branch: str
    date: str
    time: str
    guests: int
