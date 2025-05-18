from fastapi import FastAPI
from app.api import branches, menu, faq, booking, chat, validate_number
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(branches.router, prefix="/branches", tags=["Branches"])
app.include_router(menu.router, prefix="/menu", tags=["Menu"])
app.include_router(faq.router, prefix="/faq", tags=["FAQ"])
app.include_router(booking.router, prefix="/booking", tags=["Booking"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(validate_number.router, prefix="/validate_number", tags=["Number"])

