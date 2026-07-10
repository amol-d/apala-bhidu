"""Unit tests for the chat logic in ``main``.

These tests use a fake OpenAI client so no API key or network access is needed.
"""

from types import SimpleNamespace

import main


class FakeClient:
    """Minimal stand-in for the OpenAI client.

    Records the ``messages`` it was called with and returns a canned reply.
    """

    def __init__(self, reply="Namaskar bhidu!"):
        self.reply = reply
        self.calls = []
        self.chat = SimpleNamespace(
            completions=SimpleNamespace(create=self._create)
        )

    def _create(self, model, messages):
        self.calls.append({"model": model, "messages": messages})
        message = SimpleNamespace(content=self.reply)
        choice = SimpleNamespace(message=message)
        return SimpleNamespace(choices=[choice])


def test_history_to_messages_prepends_system_prompt():
    messages = main.history_to_messages([])
    assert messages == [main.SYSTEM_PROMPT]


def test_history_to_messages_converts_turns():
    history = [
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "namaste"},
    ]
    messages = main.history_to_messages(history)
    assert messages == [
        main.SYSTEM_PROMPT,
        {"role": "user", "content": "hi"},
        {"role": "assistant", "content": "namaste"},
    ]


def test_history_to_messages_handles_none():
    assert main.history_to_messages(None) == [main.SYSTEM_PROMPT]


def test_history_to_messages_skips_empty_and_unknown_roles():
    history = [
        {"role": "user", "content": ""},
        {"role": "system", "content": "ignore me"},
        {"role": "user", "content": "real message"},
    ]
    messages = main.history_to_messages(history)
    assert messages == [
        main.SYSTEM_PROMPT,
        {"role": "user", "content": "real message"},
    ]


def test_generate_reply_returns_content():
    client = FakeClient(reply="Kaay chalu aahe?")
    reply = main.generate_reply([main.SYSTEM_PROMPT], client=client)
    assert reply == "Kaay chalu aahe?"
    assert client.calls[0]["model"] == main.MODEL


def test_generate_reply_handles_none_content():
    client = FakeClient(reply=None)
    assert main.generate_reply([main.SYSTEM_PROMPT], client=client) == ""


def test_chat_fn_builds_messages_and_replies():
    client = FakeClient(reply="Sab badhiya bhidu!")
    history = [
        {"role": "user", "content": "hello"},
        {"role": "assistant", "content": "hey"},
    ]
    reply = main.chat_fn("how are you?", history, client=client)

    assert reply == "Sab badhiya bhidu!"

    sent = client.calls[0]["messages"]
    assert sent[0] == main.SYSTEM_PROMPT
    assert sent[-1] == {"role": "user", "content": "how are you?"}
    # system prompt + 2 history turns + new user message
    assert len(sent) == 4
