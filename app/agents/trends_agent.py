from datetime import datetime
from .base_agent import BaseAgent

class TrendsAgent(BaseAgent):
    def generate_insights(self, user_id: str):
        notes = self.supabase.table("notes") \
            .select("*") \
            .eq("user_id", user_id) \
            .order("created_at", desc=True) \
            .limit(10) \
            .execute().data
        
        if not notes:
            return
        
        notes_text = "\n\n".join(
            f"{note['created_at']} | {note.get('mood', '')}: {note['content'][:100]}"
            for note in notes
        )
        
        prompt = f"""
        Analyze these journal entries for trends:
        1. Mood patterns
        2. Recurring themes
        3. Suggestions for the user
        
        Entries:
        {notes_text}
        """
        
        insights = self.generate_text(prompt)
        
        self.supabase.table("user_insights").insert({
            "user_id": user_id,
            "insights": insights,
            "note_count": len(notes),
            "date_range": {
                "start": notes[-1]["created_at"],
                "end": notes[0]["created_at"]
            }
        }).execute()