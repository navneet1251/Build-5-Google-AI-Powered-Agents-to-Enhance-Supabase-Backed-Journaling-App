from .base_agent import BaseAgent

class SentimentAgent(BaseAgent):
    def process_note(self, note_id: str):
        note = self.supabase.table("notes") \
            .select("*").eq("id", note_id).execute().data[0]
        
        prompt = f"""
        Analyze the sentiment of this journal entry.
        Return 3-5 emotion tags (comma-separated):
        
        {note['content']}
        """
        
        tags = self.generate_text(prompt)
        
        self.supabase.table("notes").update({
            "tags": [t.strip() for t in tags.split(",")],
            "mood": tags.split(",")[0].strip()
        }).eq("id", note_id).execute()