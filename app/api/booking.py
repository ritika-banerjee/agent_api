from fastapi import APIRouter, HTTPException
from models.booking import BookingRequest
from core.resolver import resolve_property
import uuid

router = APIRouter()
bookings = {}

@router.post("")
def create_booking(data: BookingRequest):
    resolved = resolve_property(data.branch)
    if not resolved:
        raise HTTPException(400, detail="Could not resolve branch from input")
    
    booking_id = str(uuid.uuid4())
    bookings[booking_id] = {
        **data.model_dump(),
        "branch": resolved
    }
    return {"booking_id": booking_id, "status": "confirmed", "branch": data.branch}

@router.put("/{booking_id}")
def update_booking(booking_id: str, data: BookingRequest):
    if booking_id not in bookings:
        raise HTTPException(404, "Booking not found")
    bookings[booking_id] = data.dict()
    return {"status": "updated"}

@router.delete("/{booking_id}")
def cancel_booking(booking_id: str):
    if booking_id in bookings:
        del bookings[booking_id]
        return {"status": "cancelled"}
    raise HTTPException(404, "Booking not found")