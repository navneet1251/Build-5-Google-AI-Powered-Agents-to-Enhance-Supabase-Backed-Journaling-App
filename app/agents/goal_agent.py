from .base_agent import BaseAgent

class GoalAgent(BaseAgent):
    def process_note(self, note_id: str):
        note = self.supabase.table("notes").select("*").eq("id", note_id).execute().data[0]
        
        prompt = f"""
        Extract goals from this text. Format each as:
        - Goal: [description]
        - Confidence: [high/medium/low]
        
        Text: {note['content']}
        """
        
        goals = self._parse_goals(self.generate_text(prompt))
        
        for goal in goals:
            # Ensure confidence is valid
            confidence = goal.get("confidence", "medium").lower()
            if confidence not in ["high", "medium", "low"]:
                confidence = "medium"  # Default value
                
            self.supabase.table("goals").insert({
                "note_id": note_id,
                "user_id": note["user_id"],
                "description": goal["description"],
                "confidence": confidence  # Now guaranteed valid
            }).execute()
        
    def _parse_goals(self, text: str) -> list:
        goals = []
        current = {}
        for line in text.split("\n"):
            line = line.strip().lower()
            if line.startswith("- goal:"):
                if current:
                    goals.append(current)
                current = {"description": line.split("goal:")[1].strip()}
            elif line.startswith("- confidence:"):
                if current:
                    conf = line.split("confidence:")[1].strip()
                    current["confidence"] = conf if conf in ["high", "medium", "low"] else "medium"
        if current:
            goals.append(current)
        return goals