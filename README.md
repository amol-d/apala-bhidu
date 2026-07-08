# Apala Bhidu 🧡

A command-line AI chatbot with the personality of **Apala Bhidu** — a warm, empathetic Mumbai friend who chats in a mix of Marathi and Mumbai Hindi slang (*bhava*, *bhidu*, *dosta*, *bro*). It's supportive, a little humorous, and gives practical advice.

Built on the OpenAI Chat Completions API.

## Features

- 💬 **Interactive chat loop** — keep messaging back and forth in your terminal.
- 🧠 **Conversation memory** — the full history is sent on every turn, so the bot remembers what you said earlier.
- 🎭 **Persona-driven** — a system prompt shapes every reply into the Apala Bhidu voice.
- 🚪 **Graceful exit** — leave with `exit`, `quit`, Ctrl-C, or Ctrl-D.

## Requirements

- [Python 3.14+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) for dependency management
- An [OpenAI API key](https://platform.openai.com/api-keys)

## Setup

1. Clone the repo:

   ```bash
   git clone <repo-url>
   cd apala-bhidu
   ```

2. Install dependencies:

   ```bash
   uv sync
   ```

3. Create a `.env` file in the project root with your OpenAI key:

   ```
   OPENAI_API_KEY=sk-...your-key...
   ```

## Usage

```bash
uv run main.py
```

Then just start typing:

```
Hello from Apala Bhidu! (type 'exit' or 'quit' to leave)

You: Bhava divas jaam bakwas gela ajacha
Apala Bhidu: Are bhidu, tension nahi lene ka! Sab set ho jayega, chill maar...

You: quit
Apala Bhidu: Chal bhidu, bhetu punha! 👋
```

## Configuration

- **Model** — set in [`main.py`](main.py) on the `client.chat.completions.create(...)` call (currently `gpt-4.1-nano`).
- **Persona** — edit the `system_prompt` in [`main.py`](main.py) to change the bot's tone and character.

## Project Structure

```
apala-bhidu/
├── main.py           # Chatbot entry point (persona + chat loop)
├── pyproject.toml    # Project metadata and dependencies
├── uv.lock           # Locked dependency versions
└── .env              # Your OpenAI API key (not committed)
```
