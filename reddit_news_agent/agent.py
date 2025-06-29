from google.adk.agents import LlmAgent, Agent
from google.genai import types
import os
from google.adk.models.lite_llm import LiteLlm
from pathlib import Path
import praw
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path('.') / '.env')
from .prompts import SYSTEM_INSTRUCTION
api_key = os.getenv("OPENROUTER_API_KEY")

def get_reddit_ai_news(subreddit: str, limit: int = 5) -> dict[str, list[str]]:
    """
    Fetches top post titles from a specified subreddit using the Reddit API.

    Args:
        subreddit: The name of the subreddit to fetch news from (e.g., 'AINewsAndTrends').
        limit: The maximum number of top posts to fetch.

    Returns:
        A dictionary with the subreddit name as key and a list of
        post titles as value. Returns an error message if credentials are
        missing, the subreddit is invalid, or an API error occurs.
    """

    print(f"--- Tool called: Fetching from r/{subreddit} via Reddit API ---")
    client_id = os.getenv("REDDIT_CLIENT_ID")
    client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    user_agent = os.getenv("REDDIT_USER_AGENT")

    if not all([client_id, client_secret, user_agent]):
        print("--- Tool error: Reddit API credentials missing in .env file. ---")
        return {subreddit: ["Error: Reddit API credentials not configured."]}

    try:
        reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        # Check if the subreddit exists
        reddit.subreddits.search_by_name(subreddit, exact=True)
        sub = reddit.subreddit(subreddit)
        top_posts = list(sub.hot(limit=limit)) # Fetch hot posts
        titles = [post.title for post in top_posts]
        if not titles:
             return {subreddit: [f"No recent hot posts found in r/{subreddit}."]}
        
        return {subreddit: titles}
    
    except praw.exceptions.PRAWException as e:
        print(f"--- Tool error: {e} ---")
        return {subreddit: [f"Error fetching from r/{subreddit}: {str(e)}"]}



model = LiteLlm(
     model="openrouter/deepseek/deepseek-chat-v3-0324:free",
     api_key=api_key
     )

# root_agent = LlmAgent(
#             name="reddit_news_agent",
#             description="Agent to help users find news articles on Reddit.",
#             model=model,
#             instruction=SYSTEM_INSTRUCTION,
#             tools=[get_reddit_ai_news],
#             output_key="summary"
# )   

root_agent = Agent(
    name="reddit_news_agent",
    description="Agent to help users find news articles on Reddit.",
    model="gemini-1.5-flash-latest",
    instruction=SYSTEM_INSTRUCTION,
    tools=[get_reddit_ai_news],
    output_key="summary"
)   