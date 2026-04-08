Sure! Here’s a full README.md that explains your entire script, its setup, usage, and output—all in Markdown, ready to save as README.md:

# GeckoAssistant Chess Game Analyzer

GeckoAssistant is a Python script that fetches a collection of chess games from a Lichess player and prepares them for AI analysis. The script extracts game metadata, move lists, and splits the games into manageable chunks with a detailed AI prompt for scouting purposes.

---

## Features

- Fetches games from a specified Lichess username.
- Supports fetching up to a configurable number of recent games.
- Extracts key metadata:
  - Player names
  - Game result
  - Date
  - Opening and ECO code
  - Full moves in Standard Algebraic Notation (SAN)
- Splits games into chunks based on character limits to avoid exceeding AI input restrictions.
- Adds a comprehensive AI prompt in the first chunk to guide analysis.
- Saves each chunk as a separate `.txt` file ready for analysis.

---

## Requirements

- Python 3.10 or higher
- [berserk](https://pypi.org/project/berserk/) – Lichess API client
- [python-chess](https://pypi.org/project/python-chess/) – For parsing PGN files

Install dependencies:

```bash
pip install berserk python-chess
Setup
Get a Lichess Personal Access Token
Visit Lichess Tokens
Create a token with Read all your games permission
Configure the script

Open the script and set your variables:

API_TOKEN = "your_lichess_token_here"    # Lichess personal access token
USERNAME = "target_username_here"        # Target player to fetch games from
MAX_GAMES = 50                           # Number of games to fetch
SEPARATOR = "\n---\n"                     # Separator between games
MAX_CHARS = 15000                         # Maximum characters per chunk
CHUNK_PREFIX = USERNAME+"_chunk_"        # Prefix for chunk files

You can also edit the AI prompt to customize analysis instructions:

AI_PROMPT = """
I’m providing you with a collection of chess games played by a particular player...
"""
Usage

Run the script:

python gecko_assistant.py

What the script does:

Connects to the Lichess API using your token.
Fetches up to MAX_GAMES from the target username.
Extracts metadata and moves from each game.
Combines games into chunks without exceeding MAX_CHARS characters.
Prepends the AI prompt to the first chunk.

Saves chunks as text files with the naming convention:

USERNAME_chunk_1.txt
USERNAME_chunk_2.txt
...

During execution, the script prints progress like:

Processed game 1
Processed game 2
Saved chunk 1: 14980 characters
Saved chunk 2: 10240 characters
Done! Total chunks: 2, total games: 50
Output Example

Each game is formatted like this:

Game 1
White: Player1
Black: Player2
Result: 1-0
Date: 2023.04.01
Opening: Sicilian Defense
ECO: B40
Moves: e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 ...
---
--- separates games.
Multiple games are combined into chunks, each respecting the MAX_CHARS limit.
Notes
Keep your API token private.
Adjust MAX_GAMES and MAX_CHARS based on the size of your dataset and AI model limitations.
Ideal for feeding games into AI models for scouting and strategy analysis.
Resolves large data sets without breaking individual games.
