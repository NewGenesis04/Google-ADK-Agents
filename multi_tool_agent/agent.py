from google.adk.agents import Agent
from google.genai import types
from google.adk.tools import FunctionTool
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.tools import ToolContext
import os
import requests
from google.adk.tools import google_search
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import Union
load_dotenv()

APP_NAME = "weather_app"
USER_ID = "1234"
SESSION_ID = "session1234"

class Location(BaseModel):
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime: str

class Condition(BaseModel):
    text: str

class CurrentWeather(BaseModel):
    last_updated: str
    temp_c: float
    feelslike_c: float
    condition: Condition
    humidity: int
    wind_kph: float
    wind_dir: str
    precip_mm: float
    cloud: int
    vis_km: float
    uv: float

class WeatherAPIResponse(BaseModel):
    location: Location
    current: CurrentWeather


def get_weather(lat: str, lon: str) -> Union[str, WeatherAPIResponse]:
    """
    Fetches the current weather data for a given location based on latitude and longitude.

    Args:
        lat (str): The latitude of the location.
        lon (str): The longitude of the location.

    Returns:
        Union[str, WeatherAPIResponse]: A structured weather response or error message.

    Raises:
        str: If the request to the Weather API fails.
    """

    api_key = os.getenv("WEATHER_API_KEY")

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}&aqi=yes"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_data = WeatherAPIResponse(**data)
        # print(weather_data)
        return weather_data

    return "Sorry, I couldn’t fetch the weather."

# get_weather(lat="37.7749", lon="-122.4194")

weather_tool = FunctionTool(func=get_weather)


root_agent = Agent(
    name="weather_report_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to generate a weather report of a location."
    ),
    instruction=(
    f"""You are an assistant that provides weather reports based on user queries.
    When a user asks for the weather in a location:

    1. Use the 'google_search' tool to find the latitude and longitude of that location. 
    2. Call the 'weather_tool' tool using the retrieved latitude and longitude.
    3. Parse the response, which follows the schema: {WeatherAPIResponse}.
    4. Generate a structured weather report from the response from weather_tool.
    5. If an error occurs or data is missing, tell the user the information couldn't be found and prompt them for another location.
    """
),
    tools=[weather_tool]
    #using inbuilt and custom tools together don't work
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
            final_response = event.content.parts[0].text
            print("Agent Response: ", final_response)
    
call_agent("What is the weather in Lagos?")