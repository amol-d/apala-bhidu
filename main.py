import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "gpt-4.1-nano"
# MODEL = "gpt-5-nano"

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are Apala Bhidu, a warm and empathetic Mumbai friend. "
        "Speak naturally in a mix of Marathi and Mumbai Hindi slang. Be gender neutral unless user has mentioned its orientation "
        "Never insult or abuse the user. You can bhidu, bhava, bro wherever appropriate."
        "Be supportive, humorous when suitable, and give practical advice."
    ),
}

# Backwards-compatible alias for the previous module-level name.
system_prompt = SYSTEM_PROMPT

_client: OpenAI | None = None


def get_client() -> OpenAI:
    """Return a lazily-created OpenAI client.

    Created on first use so importing this module (e.g. from tests) does not
    require an API key to be configured.
    """
    global _client
    if _client is None:
        _client = OpenAI()
    return _client


def history_to_messages(history) -> list[dict]:
    """Convert a Gradio ``messages``-format history into an OpenAI messages list.

    ``history`` is a list of ``{"role": ..., "content": ...}`` dicts. The
    persona system prompt is always prepended.
    """
    messages: list[dict] = [SYSTEM_PROMPT]
    for turn in history or []:
        role = turn.get("role")
        content = turn.get("content")
        if role in {"user", "assistant"} and content:
            messages.append({"role": role, "content": content})
    return messages


def generate_reply(messages, client: OpenAI | None = None) -> str:
    """Call the chat completions API and return the assistant's reply text."""
    client = client or get_client()
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
    )
    return response.choices[0].message.content or ""


def chat_fn(message: str, history, client: OpenAI | None = None) -> str:
    """Gradio ``ChatInterface`` callback: reply to ``message`` given ``history``."""
    messages = history_to_messages(history)
    messages.append({"role": "user", "content": message})
    return generate_reply(messages, client=client)


def main():
    print("Hello from Apala Bhidu! (type 'exit' or 'quit' to leave)")

    messages = [SYSTEM_PROMPT]

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nApala Bhidu: Chal bhidu, bhetu punha! 👋")
            break

        if not user_input:
            continue

        if user_input.lower() in {"exit", "quit"}:
            print("Apala Bhidu: Chal bhidu, bhetu punha! 👋")
            break

        messages.append({"role": "user", "content": user_input})

        reply = generate_reply(messages)
        print(f"\nApala Bhidu: {reply}")

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()
