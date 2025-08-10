from google.adk.agents import Agent, LlmAgent
from google.adk.models.lite_llm import LiteLlm
import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.') / '.env')

api_key = os.getenv("OPENROUTER_API_KEY")

model = LiteLlm(
     model="openrouter/mistralai/mistral-7b-instruct:free",
     api_key=api_key
)

root_agent = LlmAgent(
    name="question_answering_agent",
    model=model,
    description="Agent that answers questions",
    instruction="""
    You are an agent that answers questions from your state. Make your replies conversational and engaging.
    If you don't know the answer, say 'I don't know'.
    Get the information you need from state keys:
    {name}
    {age}
    {location}
    {interests}
    {skills}
    {goals}
    {current_projects}
    {recent_achievements}
    {preferred_language}
    {preferred_tools}
    """,
    )

# qwen/qwen-2.5-7b-instruct:free
# deepseek/deepseek-chat-v3-0324:free