# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

`apala-bhidu` is a small OpenAI chat script that plays "Apala Bhidu" — a warm Mumbai friend persona that replies in a mix of Marathi and Mumbai Hindi slang. The persona is defined by the `system_prompt` in [main.py](main.py). All logic currently lives in that single file's `main()`.

## Tooling

The project is managed with **uv** (see [uv.lock](uv.lock)) and targets **Python 3.14** (see [.python-version](.python-version)).

```bash
uv sync            # install/resolve dependencies from pyproject.toml + uv.lock
uv run main.py     # run the script (loads .env, calls the OpenAI API)
```

There are no tests, linters configured to run, or build step. `isort` is a declared dependency but is not wired into any command.

## Configuration

Requires a `.env` file (gitignored) at the repo root with:

```
OPENAI_API_KEY=<key>
```

`load_dotenv()` reads it, and `OpenAI()` picks up the key from the environment automatically.

## Notes

- The model is hardcoded to `gpt-5-nano` in the `client.chat.completions.create(...)` call.
- The user message is currently hardcoded (`user_prompt`); there is no interactive input loop yet.
