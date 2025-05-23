from pydantic import BaseModel

class NoteRequest(BaseModel):
    content: str
    user_id: str

class NoteResponse(BaseModel):
    id: str
    content: str
    mood: str | None
    summary: str | None
    tags: list[str] | None