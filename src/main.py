from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from src.lib.create_connection import create_connection

from src.api.messages import messages_router

app = FastAPI(title="Whatsapp Automation API", version="0.1.0")
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def startup():
    async with create_connection():
        pass

app.add_event_handler("startup", startup)

@app.get("/", status_code=200, response_model=None)
async def redirect_to_docs():
    return RedirectResponse("/docs")

app.include_router(messages_router)