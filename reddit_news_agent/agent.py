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

import os
import praw
import prawcore

def get_reddit_ai_news(subreddit: str, limit: int = 5) -> dict[str, list[str]]:
    """
    Fetches top post titles from a specified subreddit using the Reddit API.
    """
    print(f"--- Tool called: Fetching from r/{subreddit} via Reddit API ---")
    
    # Validate limit
    if not isinstance(limit, int) or limit <= 0:
        return {subreddit: ["Error: 'limit' must be a positive integer."]}
    
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

        # Try to access subreddit
        sub = reddit.subreddit(subreddit)
        print(f"Fetching hot posts from r/{subreddit} with limit={limit}...")
        top_posts = list(sub.hot(limit=limit))
        
        titles = [post.title for post in top_posts]
        if not titles:
            return {subreddit: [f"No recent hot posts found in r/{subreddit}."]}

        return {subreddit: titles}
    
    except prawcore.exceptions.NotFound:
        return {subreddit: [f"Subreddit 'r/{subreddit}' not found."]}
    
    except prawcore.exceptions.BadRequest as e:
        return {subreddit: [f"Bad request when fetching from r/{subreddit}: {str(e)}. "
                            "Check subreddit name, limit, or API parameters."]}
    
    except praw.exceptions.PRAWException as e:
        return {subreddit: [f"PRAW error fetching from r/{subreddit}: {str(e)}"]}
    
    except Exception as e:
        return {subreddit: [f"Unexpected error fetching from r/{subreddit}: {str(e)}"]}




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