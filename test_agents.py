import os
from dotenv import load_dotenv
from app.agents import (
    SentimentAgent, SummaryAgent, 
    ReflectionAgent, GoalAgent, TrendsAgent
)

load_dotenv()

def test_all_agents():
    # 1. First create a test note in Supabase
    supabase = SentimentAgent().supabase
    test_note = supabase.table("notes").insert({
        "content": "I'm feeling anxious about my interview tomorrow but I prepared well",
        "user_id": "test_user_123"
    }).execute().data[0]
    
    note_id = test_note['id']
    user_id = test_note['user_id']
    
    print(f"Testing with note ID: {note_id}")
    
    # 2. Test each agent
    agents = {
        "Sentiment": SentimentAgent(),
        "Summary": SummaryAgent(),
        "Reflection": ReflectionAgent(),
        "Goal": GoalAgent()
    }
    
    for name, agent in agents.items():
        print(f"\n--- Testing {name}Agent ---")
        agent.process_note(note_id)
        print(f"{name} analysis completed!")
    
    # 3. Test Trends agent separately
    print("\n--- Testing TrendsAgent ---")
    TrendsAgent().generate_insights(user_id)
    print("Trends analysis completed!")
    
    # 4. Verify results
    print("\n--- Final Results ---")
    note = supabase.table("notes").select("*").eq("id", note_id).execute().data[0]
    print(f"Mood: {note.get('mood')}")
    print(f"Summary: {note.get('summary')}")
    print(f"Tags: {note.get('tags')}")
    
    reflections = supabase.table("note_reflections").select("*").eq("note_id", note_id).execute().data
    print(f"Reflection Questions: {reflections[0]['questions'] if reflections else None}")
    
    goals = supabase.table("goals").select("*").eq("note_id", note_id).execute().data
    print(f"Extracted Goals: {[g['description'] for g in goals]}")

if __name__ == "__main__":
    test_all_agents()