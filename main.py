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

user_prompt = {
    "role": "user",
    "content": "Bhava divas jaam bakwas gela ajacha"
}


def main():
    print("Hello from Apala Bhidu!")

    response = client.chat.completions.create(
        model="gpt-5-nano",
        messages=[system_prompt, user_prompt],
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()