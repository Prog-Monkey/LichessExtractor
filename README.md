# GeckoAssistant Lichess Game Scraper

This Python script fetches chess games from a Lichess player and prepares them for AI analysis. It organizes games with metadata, move lists, and splits them into manageable text chunks.

---

## Features

- Fetches games from a Lichess username.
- Extracts game metadata:
  - White & Black player names
  - Result
  - Date
  - Opening and ECO code
  - Full move list in SAN (Standard Algebraic Notation)
- Splits games into chunks to avoid exceeding character limits.
- Adds a detailed AI prompt in the first chunk for game analysis.
- Saves each chunk as a `.txt` file with a configurable prefix.

---

## Requirements

- Python 3.10+
- [berserk](https://pypi.org/project/berserk/) – Lichess API client
- [python-chess](https://pypi.org/project/python-chess/) – For parsing PGN files

Install dependencies:

```bash
pip install berserk python-chess
Setup
Get a Lichess Personal Access Token
Go to Lichess Tokens
Create a token with Read all your games permission.
Configure the script
Open the script and set:
API_TOKEN = "your_lichess_token_here"
USERNAME = "target_username_here"
MAX_GAMES = 50                 # Number of games to fetch
SEPARATOR = "\n---\n"          # Separator between games
MAX_CHARS = 15000              # Max characters per chunk
CHUNK_PREFIX = USERNAME+"_chunk_"  # Prefix for chunk files
Optional: Customize the AI prompt:
AI_PROMPT = """
I’m providing a collection of chess games played by a player. Analyze weaknesses, opening tendencies, patterns, and provide strategic advice.
"""
Usage

Run the script:

python gecko_assistant.py
The script fetches games and processes each one.
Creates text chunks containing metadata, moves, and AI prompt.
Saves files like:
USERNAME_chunk_1.txt
USERNAME_chunk_2.txt
...

Example game format inside a chunk:

Game 1
White: Player1
Black: Player2
Result: 1-0
Date: 2023.04.01
Opening: Sicilian Defense
ECO: B40
Moves: e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 ...
---
Notes
Keep your API token private.
Adjust MAX_GAMES and MAX_CHARS for dataset size and AI input limits.
Useful for feeding Lichess games into AI models for player scouting and analysis.
