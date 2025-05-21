from google.adk.agents.loop_agent import LoopAgent
from google.adk.agents.llm_agent import LlmAgent
from google.genai import types
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner

# --- Constants ---
APP_NAME = "doc_writing_app"
USER_ID = "dev_user_01"
SESSION_ID = "session_01"
GEMINI_MODEL = "gemini-2.0-flash"

# --- State Keys ---
STATE_INITIAL_TOPIC = "initial_topic"
STATE_CURRENT_DOC = "current_doc"
STATE_CRITICISM = "criticism"

state_agent = LlmAgent(
    name="StateAgent",
    model="gemini-2.0-flash-exp",
    instruction=f"""
You are a State Management AI.

Your task is to manage the topic of discussion within the session state.

Instructions:

1. If the current input provides a new topic, extract and return it.
2. If no new topic is found in the input:
   - Check if the session state already contains a value for '{STATE_INITIAL_TOPIC}'.
   - If it does, return the existing topic.
   - If it doesn't, return 'No topic found'.

Ensure that you only update the session state when a new topic is provided.
""",
    description="Parses the input and updates the topic in the session state if a new topic is provided.",
    output_key=STATE_INITIAL_TOPIC  # Saves output to state
)

writer_agent = LlmAgent(
    name="WriterAgent",
    model=GEMINI_MODEL,
    instruction=f"""
    You are a Creative Writer AI.
    Check the session state for '{STATE_CURRENT_DOC}'.
    If '{STATE_CURRENT_DOC}' does NOT exist or is empty, write a very short (1-2 sentence) story or document based on the topic in state key '{STATE_INITIAL_TOPIC}'.
    If '{STATE_CURRENT_DOC}' *already exists* and '{STATE_CRITICISM}', refine '{STATE_CURRENT_DOC}' according to the comments in '{STATE_CRITICISM}'."
    Output *only* the story or the exact pass-through message.
    """,
    description="Writes the initial document draft.",
    output_key=STATE_CURRENT_DOC # Saves output to state
)

# Critic Agent (LlmAgent)
critic_agent = LlmAgent(
    name="CriticAgent",
    model=GEMINI_MODEL,
    instruction=f"""
    You are a Constructive Critic AI.
    Review the document provided in the session state key '{STATE_CURRENT_DOC}'.
    Provide 1-2 brief suggestions for improvement (e.g., "Make it more exciting", "Add more detail").
    Output *only* the critique.
    """,
    description="Reviews the current document draft.",
    output_key=STATE_CRITICISM # Saves critique to state
)

# Create the LoopAgent
root_agent = LoopAgent(
    name="LoopAgent", sub_agents=[state_agent, writer_agent, critic_agent], max_iterations=3
)

# Session and Runner
session_service = InMemorySessionService()
session = session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)

# Agent Interaction
def call_agent(query):
    content = types.Content(role='user', parts=[types.Part(text=query)])
    events = runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    for event in events:
        if event.is_final_response():
            agent_name = event.author
            final_response = event.content.parts[0].text
            print(f"{agent_name} Response: ", final_response)

call_agent("execute")