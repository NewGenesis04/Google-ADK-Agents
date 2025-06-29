from google.adk.agents import Agent
import os
from google.adk.agents import LlmAgent
from .prompt import EMAIL_DESCRIPTION
from .schemas import EmailContent
from google.adk.models.lite_llm import LiteLlm
from google.genai import types
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.') / '.env')


api_key = os.getenv("OPENROUTER_API_KEY")
model = LiteLlm(
     model="openrouter/google/gemma-3n-e4b-it:free",
     api_key=api_key
     )

root_agent = LlmAgent(
    name="email_writer_agent",
    model=model,
    description="Agent to write structured professional emails",
    instruction=EMAIL_DESCRIPTION,
    output_schema=EmailContent,
    output_key="email_content",
)