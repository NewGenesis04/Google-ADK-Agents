from google.adk.agents import LlmAgent, SequentialAgent
from google.genai import types
import os
from google.adk.models.lite_llm import LiteLlm
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.') / '.env')

api_key = os.getenv("OPENROUTER_API_KEY")
model = LiteLlm(
     model="openrouter/meta-llama/llama-3.2-3b-instruct:free",
     api_key=api_key
     )

root_agent = LlmAgent(
            name="exam_prep_agent",
            description="Agent to help prepare students for exams.",
            model=model,
            instruction="",
            output_key=""
)