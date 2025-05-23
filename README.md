# Build-5-Google-AI-Powered-Agents-to-Enhance-Supabase-Backed-Journaling-App
Design and implement 5 intelligent agents using Google AI (Gemini, PaLM API, etc.) that operate on notes stored in Supabase. These agents should extract meaning, suggest insights, or provide helpful actions to improve the user’s journaling and productivity experience.

# Journaling App with AI Analysis Agents

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green.svg)
![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-orange.svg)
![Docker](https://img.shields.io/badge/Docker-Container-blue.svg)

A backend system that automatically analyzes journal entries using Google Gemini AI to provide insights through 5 specialized agents.

## ✨ Features

- **Sentiment Analysis**: Detects mood/emotions in entries
- **Smart Summarization**: Generates concise summaries
- **Reflection Prompts**: Suggests thought-provoking questions
- **Goal Extraction**: Identifies actionable intentions
- **Trend Insights**: Finds patterns across multiple entries
- **REST API**: FastAPI endpoints for easy integration
- **Docker Support**: Ready for containerized deployment

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Backend Framework | FastAPI |
| Database | Supabase (PostgreSQL) |
| AI Provider | Google Gemini API |
| Containerization | Docker |
| Testing | Postman |

## 📂 Project Structure

```text
journal-app/
├── app/
│ ├── agents/ # AI analysis modules
│ │ ├── base_agent.py # Shared functionality
│ │ ├── sentiment_agent.py
│ │ └── ... (4 more agents)
│ ├── models.py # Data validation
│ └── main.py # API endpoints
├── tests/ # Test scripts
├── Dockerfile # Container config
├── requirements.txt # Dependencies
└── .env.example # Configuration template
```


## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Supabase account
- Google AI API key

### Local Setup
1. Clone repository
2. Set up environment
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run FastAPI server:
```bash
uvicorn app.main:app --reload
```
5. Docker Deployment
```bash
docker build -t journal-app .
docker run -p 8000:8000 --env-file .env journal-app
```


