from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime
from google.adk.tools import FunctionTool
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.') / '.env')

api_key = os.getenv("OPENROUTER_API_KEY")

model = LiteLlm(
     model="openrouter/qwen/qwen-2.5-7b-instruct:free",
     api_key=api_key
)

root_agent = Agent(
    name="joker_agent",
    model=model,
    description="Agent to tell jokes",
    instruction="You are an agent that tells jokes.",
)