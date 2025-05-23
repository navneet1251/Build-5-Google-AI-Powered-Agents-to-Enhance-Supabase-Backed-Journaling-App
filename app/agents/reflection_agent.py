from .base_agent import BaseAgent

class ReflectionAgent(BaseAgent):
    def process_note(self, note_id: str):
        note = self.supabase.table("notes") \
            .select("*").eq("id", note_id).execute().data[0]
        
        prompt = f"""
        Generate 3 reflective questions about:
        {note['content']}
        Format each with "- " prefix
        """
        
        questions = [
            q.strip("- ") 
            for q in self.generate_text(prompt).split("\n") 
            if q.strip()
        ]
        
        self.supabase.table("note_reflections").insert({
            "note_id": note_id,
            "questions": questions,
            "user_id": note["user_id"]
        }).execute()