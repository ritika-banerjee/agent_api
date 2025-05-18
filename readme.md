Barbeque Nation Voice AI - Technical Documentation  
Author: Ritika  
Tools Used: FastAPI, RetellAI, FAISS, Python

Overview:
---------
This project implements a voice-based conversational agent for Barbeque Nation using RetellAI. 
The agent is capable of handling customer queries, answering FAQ-related questions, 
fetching menu details, returning branch-specific information (timings, offers, amenities), 
and handling booking-related workflows such as booking, modifying, or cancelling reservations.

Although full integration with RetellAI function-calling was not completed due to platform limitations, 
the agent behavior was replicated and tested using custom-built APIs and a structured, token-efficient knowledge base.


Directory Structure:
--------------------
The codebase follows a clean separation of concerns between APIs, core logic, and data models.

- /api
  Contains all API endpoints exposed via FastAPI.

  - booking.py             → Handles table booking, modification, and cancellation.
  - branches.py            → Returns outlet-specific data like timings, offers, amenities, etc.
  - chat.py                → Manages chatbot message handling and logic (used for simulation/testing).
  - faq.py                 → Returns FAQ-style KB responses, supports chunk_id and topic routing.
  - menu.py                → Returns veg/non-veg menu items per course (starter, main, dessert).
  - validate_number.py     → Validates customer contact numbers for booking.

- /core
  Contains business logic and shared functionality.

  - faiss_index.py         → Implements FAISS-based semantic search on top of vectorized knowledge base chunks.
  - kb_loader.py           → Loads and caches JSON knowledge base for use across the app.
  - resolver.py            → Maps natural language outlet names (e.g. "cp", "jp nagar") to internal property keys using alias mapping.

- /models
  Contains Pydantic models used for request/response validation and documentation.

  - booking.py             → Models for booking payloads.
  - chat.py                → Request/response schema for chat-based testing or fallback queries.
  - faq.py                 → FAQ schema (chunk_id, question, answer).
  - val_num.py             → Contact number validation model.

Core Functionality:
-------------------
1. Cleaned and structured knowledge base from raw .docx and .pdf into JSON chunks
   under 800 tokens (for compatibility with Retell function calling limits).
   Includes branches data, menu, offers, alerts, and 20+ FAQ entries.

2. Built a property name resolver using alias mapping to handle fuzzy outlet names like
   “connaught place”, “rajiv chowk”, “koramangala first block” → mapped to internal property keys
   like “bbq_cp_delhi”, “bbq_koromangala_1st_block” etc.

3. Developed a RESTful API structure with:
   - /kb/branch: Accesses structured outlet data (timings, offers, amenities).
   - /kb/faq: Returns precise FAQ responses using topic and chunk_id routing.
   - /kb/menu: Accesses veg/non-veg menu data by course.
   - /kb/resolve: Maps user input (natural language outlet name) to internal keys.

4. Implemented caching (via `lru_cache`) to ensure high performance and reduce disk I/O.

5. Integrated FAISS for semantic search on KB chunks. This allows the agent to return
   fuzzy-matched answers even when an exact chunk_id is not available.
   FAISS uses vectorized knowledge base entries and cosine similarity search to retrieve the best answer.

Retell Agent:
-------------
A RetellAI agent was created to simulate the booking and enquiry flows. 
While direct API function calling could not be fully wired into Retell due to time constraints,
agent performance was tested using local endpoint responses and Retell prompt logic.

Retell Agent Capabilities:
- Answer user questions using cleaned KB data.
- Guide users through reservation.
- Provide fallback and clarification in case of ambiguity.
- Handles outlet-specific logic via prompts and structured responses.

Achievements:
-------------
- Successfully implemented a real-world, API-driven voice assistant framework.
- Cleaned and token-optimized knowledge base from unstructured documents.
- Created a scalable KB server with routing, caching, and fallback logic.
- Simulated a full conversational agent with FAISS search and prompt handling.

Limitations:
------------
- RetellAI agent is not fully connected to the FastAPI backend using function calling, due to external constraints.
- UI/chat frontend not implemented (voice-focused).
- Menu switching logic could be improved further using context chaining in Retell.

Instructions to Run:
--------------------
1. Install dependencies:
   pip install -r requirements.txt

2. Run the server:
   uvicorn main:app --reload

3. Access endpoints like:
   - /kb/faq?topic=menu_and_drinks&chunk_id=menu_q2
   - /kb/menu?type=veg&course=starter
   - /kb/branch?property=bbq_cp_delhi&topic=timings
   - /kb/resolve?name=jp nagar

4. Test FAISS search with:
   - curl -X POST /chat/search with a query body like "do you serve jain food?"

Conclusion:
-----------
This system is modular, production-ready, and designed with real-world agent workflows in mind.
With better API-agent integration, this backend can power a fully autonomous customer voice assistant for Barbeque Nation.
