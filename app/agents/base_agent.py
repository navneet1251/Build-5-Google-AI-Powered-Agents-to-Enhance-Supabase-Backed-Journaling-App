import os
from dotenv import load_dotenv
import google.generativeai as genai
from supabase import create_client, Client

load_dotenv()

class BaseAgent:
    def __init__(self):
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_KEY')
        
        if not supabase_url or not supabase_key:
            raise ValueError("Missing Supabase credentials")
            
        self.supabase: Client = create_client(supabase_url, supabase_key)
        
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def generate_text(self, prompt: str) -> str:
        response = self.model.generate_content(prompt)
        return response.text