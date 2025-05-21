from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time() -> str:
    """
    Returns the current date and time in ISO 8601 format.
    """
    return {
      "current_time": datetime.now().isoformat()
    }

# root_agent = Agent(
#    # A unique name for the agent.
#    name="basic_search_agent",
#    # The Large Language Model (LLM) that agent will use.
#    model="gemini-2.0-flash",
#    description="Agent to answer questions using Google Search.",
#    instruction="You are an expert researcher. You always stick to the facts.",
#    tools=[google_search]
# )

root_agent = Agent(
   # A unique name for the agent.
   name="basic_time_agent",
   # The Large Language Model (LLM) that agent will use.
   model="gemini-2.0-flash",
   description="Agent to answer get_current time",
   instruction="You are an agent that provides the current time.",
   tools=[get_current_time]
)