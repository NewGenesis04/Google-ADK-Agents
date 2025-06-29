# Reddit News Agent

This project contains an AI-powered agent that fetches and summarizes news headlines from Reddit, specifically focused on artificial intelligence (AI) topics. The agent uses the Reddit API (via `praw`) and can be integrated with LLMs for enhanced conversational capabilities.

---

## Features

- **Fetches top post titles** from any specified subreddit (default: `r/AINewsAndTrends`).
- **Summarizes and formats** the news as a bulleted list.
- **Handles errors gracefully** (e.g., missing credentials, invalid subreddit).
- **Configurable LLM backend** (supports Gemini and DeepSeek via OpenRouter).
- **Environment variable support** for API keys and credentials.

---

## Folder Structure

reddit_news_agent/
                 ├──__init__.py 
                 ├── agent.py # Main agent logic and Reddit tool
                 ├── prompts.py # System prompt/instructions for the agent


---
## Requirements
- At least Python 3.10+
- **pip** as dependency manager

---
## Setup

1. **Clone the repository** and navigate to the project folder.

2. **Install dependencies** (in your virtual environment):
   ```bash
   pip install -r requirements.txt

3. **Configure your** .env **file** in the project root with the following variables:
OPENROUTER_API_KEY=your_openrouter_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_app_name/0.1 by your_reddit_username
GOOGLE_API_KEY=your_google_api_key

## Usage
1. Enter your terminal and run the agent via the command:
```
    adk web
```
2. Select the reddit_news_agent from the agent menu and start chatting with it.
