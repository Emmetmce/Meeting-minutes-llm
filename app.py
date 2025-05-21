#fastAPI entrypoint
import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set in .env or environment")
client = OpenAI(api_key=api_key)

from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import json
import traceback
app = FastAPI()

def gen_summary(transcript: str) -> str:
    prompt = f"Summarize this meeting transcript in three bullet points:\n\n{transcript}"
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content.strip()

def extract_action_items(transcript: str) -> list[dict]:
    prompt = ("From this transcript, extract all action items as a JSON array of "
              "`{\"task\": string, \"owner\": string, \"due_date\": string}`. "
              "If a field isn’t mentioned, set it to null.\n\n"
              f"{transcript}")
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    text = resp.choices[0].message.content.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return [{"error": text}]

class Result(BaseModel):
    summary: str
    action_items: list[dict]

@app.post("/process_transcript/", response_model=Result)
async def process_transcript(file: UploadFile = File(...)):
    try:
        # 1) Read & decode
        raw = await file.read()
        transcript = raw.decode("utf-8")
        print("Transcript loaded, length:", len(transcript))

        # 2) get ai summary
        summary = gen_summary(transcript)
        print("Summary response (first 100 chars):", summary[:100])

        # 3) Call GPT for action items
        actions = extract_action_items(transcript)
        print("Action‐items response:", actions)

        return Result(summary=summary, action_items=actions)

    except Exception as e:
        # print full traceback in terminal
        traceback.print_exc()
        # return the error text in the HTTP response
        raise HTTPException(status_code=500, detail=str(e))