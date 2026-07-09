import os

from dotenv import load_dotenv
from openai import OpenAI
import tiktoken

load_dotenv()

client = OpenAI()
model = "gpt-4.1-nano"
# model="gpt-5-nano"
encoding = tiktoken.encoding_for_model("gpt-4.1-mini")
system_prompt = {
    "role": "system",
    "content": (
        "You are Apala Bhidu, a warm and empathetic Mumbai friend. "
        "Speak naturally in a mix of Marathi and Mumbai Hindi slang. Be gender neutral unless user has mentioned its orientation "
        "Never insult or abuse the user. You can bhidu, bhava, bro wherever appropriate."
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

        # for i in  messages:
        #     tokens = encoding.encode(i['content'])
        #     print(f"input token used ${tokens}")

        response = client.chat.completions.create(
            model=model,
            messages=messages,
        )

        reply: str = response.choices[0].message.content or ''
        print(f"\nApala Bhidu: {reply}")
        # tokens = encoding.encode(reply)
        # print(f"output token used ${tokens}")

        messages.append({"role": "assistant", "content": reply})


if __name__ == "__main__":
    main()