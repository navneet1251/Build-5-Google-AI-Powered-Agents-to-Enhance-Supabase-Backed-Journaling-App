from .base_agent import BaseAgent

class SummaryAgent(BaseAgent):
    def process_note(self, note_id: str):
        note = self.supabase.table("notes") \
            .select("*").eq("id", note_id).execute().data[0]
        
        prompt = f"Summarize this in one sentence: {note['content']}"
        summary = self.generate_text(prompt).strip('"\'')

        self.supabase.table("notes") \
            .update({"summary": summary}) \
            .eq("id", note_id).execute()