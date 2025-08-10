# 🕑 Reminder Agent

Welcome to **Reminder Agent** – your friendly, persistent, and slightly quirky AI assistant that never forgets (unless you tell it to)! This agent helps you manage your reminders, remember your name, and keep your life organized, all while chatting in clear, concise English.

---

## 🚀 Features

- **Add Reminders:** Tell the agent what you need to remember, and it’ll store it for you.
- **View Reminders:** Forgot what you asked it to remember? Just ask!
- **Update Reminders:** Plans change? No problem – update any reminder by its number or content.
- **Delete Reminders:** Remove reminders you no longer need, with a simple command.
- **Name Recognition:** Introduce yourself, and the agent will remember your name for a personal touch.
- **Persistent Memory:** Reminders and your name are stored in a database, so nothing gets lost between sessions.
- **Conversational & Friendly:** The agent always responds in English, keeps things concise, and never overloads you with info.

---

## 🛠️ How It Works

- **Stateful AI:** Uses Google ADK’s session and state management to remember you and your reminders.
- **Tools:** Custom tools for adding, viewing, updating, and deleting reminders, plus updating your name.
- **Database Storage:** Reminders are saved in a local SQLite database (`reminder_agent_data.db`) for persistence.
- **Terminal Chat:** Interact with the agent via a fun, colorful terminal chat loop.

---

## 📂 Folder Structure

```
reminder_agent/
├── __init__.py
├── agent.py         # The main agent definition
├── main.py          # Interactive terminal chat with the agent
├── prompt.py        # System instructions for the agent
├── tools.py         # All reminder management tools
├── reminder_agent_data.db  # SQLite database for persistent storage
└── README.md        # (You are here!)
```

---

## ⚡ Quickstart

1. **Install dependencies**  
   Make sure you have Python 3.10+ and run:
   ```bash
   pip install -r ../requirements.txt
   ```

2. **Set up your `.env` file**  
   Place your `.env` in the project root (see [requirements.txt](../requirements.txt) for needed packages).  
   For this agent, you mainly need your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

3. **Run the agent!**
   ```bash
   python main.py
   ```

4. **Chat away!**  
   - Add reminders: `Remind me to buy milk`
   - View reminders: `What are my reminders?`
   - Update reminders: `Change my first reminder to call mom`
   - Delete reminders: `Delete reminder 2`
   - Set your name: `My name is Alex`

---

## 🧠 How the Agent Thinks

- **Always English:** No non-English words, ever!
- **Smart Matching:** If you say “delete my meeting reminder,” it’ll find the closest match.
- **User-Friendly Indexing:** Reminders are numbered starting at 1 (not 0).
- **No Clarification Requests:** The agent uses its best guess – it won’t ask you to clarify which reminder you meant.
- **Polite & Concise:** Keeps responses short and sweet, and always addresses you by name if it knows it.

---

## 📝 Customization

Want to tweak how reminders are handled?  
Check out [`tools.py`](tools.py) for all the logic, or update the system prompt in [`prompt.py`](prompt.py) for a different personality.

---

## 💡 Example Session

```
Welcome to Reminder Agent Chat!
Your reminders will be remembered across conversations.
Type 'exit' or 'quit' to end the conversation.

You: Remind me to water the plants
Agent: Added reminder: water the plants

You: What are my reminders?
Agent: 1. water the plants

You: My name is Jamie
Agent: Updated your name to: Jamie

You: Delete my plants reminder
Agent: Deleted reminder 1: 'water the plants'
```

---

## 🦸‍♂️ Credits

Built with [Google ADK](https://github.com/google/adk-python), a dash of Python, and a sprinkle of fun.

---
