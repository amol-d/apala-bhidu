import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = {
    "role": "system",
    "content": (
        "You are Apala Bhidu, a warm and empathetic Mumbai friend. "
        "Speak naturally in a mix of Marathi and Mumbai Hindi slang. "
        "Use words like bhava, bhidu, dosta, bro where appropriate. "
        "Never insult or abuse the user. "
        "Be supportive, humorous when suitable, and give practical advice."
    ),
}


def main():
    print("Hello from Apala Bhidu! (type 'exit' or 'quit' to leave)")

    messages = [system_prompt]

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

        response = client.chat.completions.create(
            # model="gpt-5-nano",
            model="gpt-4.1-nano",
            messages=messages,
        )

        reply = response.choices[0].message.content
        print(f"\nApala Bhidu: {reply}")

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()