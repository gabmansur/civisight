from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import politicians

app = FastAPI(
    title="Civisight API",
    description="An AI-powered political insight platform for civic transparency.",
    version="0.1.0",
)

# Allow frontend connections (adjust origins later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(politicians.router, prefix="/politicians", tags=["Politicians"])

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Civisight API!",
        "routes": ["/politicians"]
    }