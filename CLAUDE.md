# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`apala-bhidu` is an OpenAI chat application that plays "Apala Bhidu" — a warm Mumbai friend persona that replies in a mix of Marathi and Mumbai Hindi slang. The persona is defined by `SYSTEM_PROMPT` in [main.py](main.py).

There are two front-ends over the same chat logic:

- [main.py](main.py) — the reusable chat logic plus a terminal REPL (`main()`).
- [app.py](app.py) — a Gradio `ChatInterface` web UI that calls `chat_fn` from `main.py`.

## Tooling

The project is managed with **uv** (see [uv.lock](uv.lock)) and targets **Python 3.14** (see [.python-version](.python-version)).

```bash
uv sync            # install/resolve dependencies from pyproject.toml + uv.lock
uv run main.py     # run the terminal REPL (loads .env, calls the OpenAI API)
uv run app.py      # launch the Gradio web chat UI (prints a local URL)
uv run pytest      # run the unit tests in tests/
```

`pytest` is declared in the `dev` dependency group and configured under
`[tool.pytest.ini_options]` (adds the repo root to `pythonpath`, tests live in
`tests/`). The tests use a fake OpenAI client, so they need no API key or
network access. No linters are wired into any command; `isort` is a declared
dependency but is not run automatically.

## Configuration

Requires a `.env` file (gitignored) at the repo root with:

```
OPENAI_API_KEY=<key>
```

`load_dotenv()` reads it, and `OpenAI()` picks up the key from the environment automatically.

## Notes

- The model is set once via the module-level `MODEL` constant in [main.py](main.py) (currently `gpt-4.1-nano`).
- The OpenAI client is created lazily via `get_client()` so importing `main` (e.g. from tests) does not require an API key.
- Chat logic in `main.py` is split into small, testable functions:
  - `history_to_messages(history)` — turns a Gradio `messages`-format history into an OpenAI messages list, prepending `SYSTEM_PROMPT`.
  - `generate_reply(messages, client=None)` — calls the API and returns the reply text.
  - `chat_fn(message, history, client=None)` — the Gradio `ChatInterface` callback; also the seam tests inject a fake client through.
- `main()` runs an interactive REPL loop: it reads user input, appends each turn to a `messages` list (so the full conversation history is sent on every request for context), and exits on `exit`/`quit`, EOF, or Ctrl-C.
- `app.py` targets **Gradio 6** (messages format is the default; the `type="messages"` argument was removed).
