# 📰 Reddit News Agent

Welcome to **Reddit News Agent** – your always-curious, never-sleepy AI that fetches the latest and greatest from Reddit, so you don’t have to scroll endlessly! Whether you want trending headlines, niche subreddit gems, or just a daily dose of internet culture, this agent’s got you covered.

---

## 🚀 Features

- **Fetch Top Reddit News:** Instantly get the hottest posts from your favorite subreddits.
- **Customizable Sources:** Ask for news from any subreddit – tech, science, worldnews, memes, you name it!
- **Summarized Headlines:** The sagent delivers concise, easy-to-read summaries (no clickbait, just the good stuff).
- **Conversational & Friendly:** Always responds in clear, concise English with a dash of personality.
- **No Reddit Account Needed:** Just run and chat – no login or API keys required for basic usage.

---

## 🛠️ How It Works

- **Agent Core:** The magic lives in `agent.py`, where the agent interprets your requests and fetches Reddit content.
- **Prompt Engineering:** `prompts.py` contains the system instructions and prompt templates that keep the agent on track and in character.
- **Plug-and-Play:** Just run the agent and start chatting – it handles the rest!

---

## 📂 Folder Structure

```
reddit_news_agent/
├── __init__.py
├── agent.py      # The main agent logic
├── prompts.py    # System prompts and instructions
├── README.md     # (You are here!)
└── __pycache__/  # Compiled Python files
```

---

## ⚡ Quickstart

1. **Install dependencies**  
   Make sure you have Python 3.10+ and run:
   ```bash
   pip install -r ../requirements.txt
   ```

2. **Run the agent!**
   - Navigate to the root folder on your terminal and run one of the following commands:
   ---
   Run in CLI
   ```bash
   adk run reddit_news_agent
   ```
   ---
   Run on web:
   ```bash
   adk web
   ```

4. **Start chatting!**  
   - Get top news: `What's trending on r/worldnews?`
   - Ask for tech: `Show me the latest from r/technology`
   - Explore fun: `What's hot on r/funny today?`
   - Get summaries: `Summarize the top posts from r/science`

---

## 🧠 How the Agent Thinks

- **Always English:** No non-English words, ever!
- **Summarizes, Not Spams:** Gives you the highlights, not a wall of text.
- **Subreddit Smart:** Knows how to fetch and filter posts from any subreddit you mention.
- **Polite & Fun:** Keeps things light, friendly, and never boring.

---

## 📝 Customization

Want to change how the agent summarizes or which subreddits it prefers?  
Edit [`prompts.py`](prompts.py) for personality tweaks, or dive into [`agent.py`](agent.py) to adjust fetching and formatting logic.

---

## 💡 Example Session

```
You: What's trending on r/news?
Agent: Here are the top 3 posts from r/news:
1. "Major breakthrough in renewable energy" (2.1k upvotes)
2. "Global leaders meet for climate summit" (1.8k upvotes)
3. "New tech aims to clean oceans" (1.5k upvotes)

You: Show me something fun from r/aww!
Agent: Top post from r/aww: "Puppy learns to climb stairs for the first time" (3.2k upvotes)
```

---

## 🦸‍♂️ Credits

Built with Python, Reddit’s open API, and a love for internet news.

---

Stay curious, stay
