from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
import os
import asyncio
from agent import root_agent
load_dotenv()


session_service = InMemorySessionService()


initial_state = {
    'name': "Ogie Omorose",
    'age': 21,
    'location': "Lagos, Nigeria",
    'interests': ["AI", "Technology", "Music"],
    'skills': ["Python", "Machine Learning", "Data Analysis"],
    'goals': ["Become an AI expert", "Contribute to open-source projects", "Learn more about quantum computing"],
    'current_projects': ["Developing a personal AI assistant", "Contributing to an open-source AI project"],
    'recent_achievements': ["Completed a machine learning course", "Built a simple AI model"],
    'preferred_language': "English",
    'preferred_tools': ["Python", "FastAPI", "Pandas"],
}

APP_NAME = "Ogie's Bot"
USER_ID = "ogie_omorose"
SESSION_ID = "session_1"

async def setup_session_and_runner():
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state,
        session_id=SESSION_ID
    )

    runner = Runner(
        app_name=APP_NAME,
        agent=root_agent,
        session_service=session_service,  
    )
    return runner


async def call_agent():
    content = types.Content(role='user', parts=[types.Part(text='Where do I live?')])
    runner = await setup_session_and_runner()
    events = runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
            new_message=content)
    
    final_response=None
    
    async for event in events:
        if event.content and event.content.parts:
            if event.is_final_response():
                final_response = event.content.parts[0].text

    if final_response:
            print(f"Agent Response: {final_response}")
    else:
            print("Agent did not produce a final response.")


async def main():
    await call_agent()

if __name__ == "__main__":
    asyncio.run(main())