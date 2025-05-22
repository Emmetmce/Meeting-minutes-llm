#fastAPI entrypoint
import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not set in .env")
client = OpenAI(api_key=api_key)

from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from pydantic import BaseModel
import json
import traceback
from prototypes.prompts import prompts

app = FastAPI()
class Result(BaseModel):
    summary: str
    action_items: list[dict]

#recieve type of transcript for prompt
@app.post("/process_transcript/", response_model=Result)
async def process_transcript(
    file: UploadFile = File(...),
    meeting_type: str = Form(...),              
):
    #read it
    raw = await file.read()
    transcript = raw.decode("utf-8")

    #pick prompt
    summ_prompt = prompts[meeting_type]["summary"].format(transcript=transcript)
    actions_prompt = prompts[meeting_type]["actions"].format(transcript=transcript)

    #call gpt
    summ_resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": summ_prompt}]
    )

    summ = summ_resp.choices[0].message.content.strip()

    actions_resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": actions_prompt}]
    )
    actions_text = actions_resp.choices[0].message.content.strip()

    #parse json
    try:
        action_items = json.loads(actions_text)
    except json.JSONDecodeError:
        action_items = [{"error": actions_text}]

    return Result(summary=summ, action_items=action_items)