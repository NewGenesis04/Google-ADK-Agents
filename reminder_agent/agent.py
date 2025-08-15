from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
import os
from pathlib import Path
from dotenv import load_dotenv
from prompt import SYSTEM_INSTRUCTION
from tools import add_reminder, delete_reminder, view_reminders, update_reminder, update_user_name
load_dotenv(dotenv_path=Path('.') / '.env')

api_key = os.getenv("OPENROUTER_API_KEY")

model = LiteLlm(
     model="openrouter/moonshotai/kimi-k2:free",
     api_key=api_key
)

root_agent = LlmAgent(
                        name= "Reminder_Agent",
                        description= "A smart reminder agent with persistent memory",
                        instruction=SYSTEM_INSTRUCTION,
                        model=model,
                        tools=[
                            add_reminder,
                            delete_reminder,
                            view_reminders,
                            update_reminder,
                            update_user_name
                        ]
                    )