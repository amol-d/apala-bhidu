"""Gradio chat UI for Apala Bhidu.

Run with:

    uv run app.py

Then open the printed local URL in a browser.
"""

import gradio as gr

from main import chat_fn

CHATBOT = gr.Chatbot(
    label="Apala Bhidu",
    height=500,
    placeholder="Bol bhidu, kya haal hai? 🙌",
)

demo = gr.ChatInterface(
    fn=chat_fn,
    chatbot=CHATBOT,
    title="Apala Bhidu 👨‍💼",
    description=(
        "Tumcha Mumbai wala dost. Bindhaast bol — Marathi, Hindi, English, "
        "kahi bhi chalega."
    ),
    examples=[
        "Aaj mood off hai yaar",
        "Interview ke liye tips de na",
        "Weekend pe kya karu Mumbai mein?",
    ],
)


if __name__ == "__main__":
    demo.launch()
