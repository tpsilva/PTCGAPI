# Pokémon Card API

A small Python project that loads card data from JSON files in the `data/` directory and exposes a minimal FastAPI endpoint to look up a card's name and category by language.

## Requirements

- Python 3.12+
- See `requirements.txt` for the pinned third-party packages (FastAPI).

## Install

Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the app

Start the FastAPI server in dev mode:

```bash
fastapi dev main.py
```

The server will load all JSON files from the `data/` directory at startup.

## Example

Request:

```bash
curl http://127.0.0.1:8000/cards/en/SSP/238
```

The endpoint constructs the internal card id as `{set}-{id}` (for example `SSP-238`) and will return either the card data (id, category and localized name) or a 404-style error object. Example success response:

```json
{"id":"SSP-238","category":"Pokemon","name":"Pikachu ex"}
```
