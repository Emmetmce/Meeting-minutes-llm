# Meeting-Transcript-Processor

This project is a web app that processes meeting or press conference transcripts to generate summaries (specific to the type of transcript) and extract actionable items. It combines a FastAPI backend with a streamlit frontend and uses OpenAI's GPT models for natural language processing.

# Features

- Summarization: Generates 3-bullet summary of uploaded transcript
- Action Item Extraction: Identifies tasks, assigns owners, and tracks due dates. 

- FastAPI Backend: Handles transcript processing and GPT integration. 
- Streamlit Frontend: UI for uploading transcript and viewing results. 

# Running Instructions

    Confirm requirements with pip install -r requirements.txt

1. Create virtual environment: source venv/bin/activate

2. Start backend: uvicorn app:app --reload

3. Launch frontend: streamlit run ui.py



Upload transcript -> fastAPI ingestion -> Prompts -> UI 
