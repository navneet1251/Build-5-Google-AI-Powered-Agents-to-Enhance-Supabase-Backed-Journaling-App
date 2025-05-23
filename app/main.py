from fastapi import FastAPI, HTTPException
from .models import NoteRequest, NoteResponse
from .agents import (
    SentimentAgent, SummaryAgent,
    ReflectionAgent, GoalAgent, TrendsAgent
)
# import logging

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)


app = FastAPI()

@app.post("/notes/", response_model=NoteResponse)
async def create_note(note: NoteRequest):
    """Create and analyze a new note"""
    supabase = SentimentAgent().supabase
    new_note = supabase.table("notes").insert({
        "content": note.content,
        "user_id": note.user_id
    }).execute().data[0]
    
    # Trigger all agents
    note_id = new_note['id']
    SentimentAgent().process_note(note_id)
    SummaryAgent().process_note(note_id)
    ReflectionAgent().process_note(note_id)
    GoalAgent().process_note(note_id)
    
    return new_note

@app.get("/notes/{note_id}", response_model=NoteResponse)
async def get_note(note_id: str):
    """Retrieve a processed note"""
    note = SentimentAgent().supabase.table("notes") \
        .select("*").eq("id", note_id).execute().data
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note[0]

@app.post("/analyze/trends/{user_id}")
async def analyze_trends(user_id: str):
    """Generate insights from user's notes"""
    TrendsAgent().generate_insights(user_id)
    return {"status": "Trends analysis completed"}