import berserk
import chess.pgn
from io import StringIO

# --- CONFIG ---
API_TOKEN = ""  # Your Lichess personal access token
USERNAME = ""               # Target username
MAX_GAMES = 50                           # Number of games to fetch
SEPARATOR = "\n---\n"                    # Separator between games
MAX_CHARS = 15000                        # Max characters per chunk
CHUNK_PREFIX = USERNAME+"_chunk_"    # Prefix for chunk files

# AI prompt to go at the top of the first chunk
AI_PROMPT = """
I’m providing you with a collection of chess games played by a particular player. Each game includes metadata like players’ names, results, dates, openings, and the full move list in standard algebraic notation.

Please analyze these games carefully and provide a comprehensive scouting report covering the following points:

1. Weaknesses: Identify specific recurring weaknesses or mistakes the player tends to make (e.g., typical blunders, time management issues, poor endgame technique, tactical oversights).
2. Opening Tendencies: Summarize the openings and defenses the player frequently chooses, and identify which openings or variations they struggle against or often lose to.
3. Traps and Patterns: Point out any common tactical traps or recurring patterns where the player falls into trouble.
4. Strategic Advice: Suggest specific openings and lines I should play to exploit their weaknesses and maximize my winning chances.
5. General Style: Describe the player’s general playing style (aggressive, passive, positional, tactical) based on their games.
6. Any Additional Insights: Provide any other useful observations or advice that could help me prepare against this opponent.

Analyze based solely on the games provided below.
"""

# --- Initialize Lichess client ---
session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session)

# --- Scrape games and create a list of game texts ---
games_list = []

for game_index, game in enumerate(client.games.export_by_player(USERNAME, max=MAX_GAMES, as_pgn=True), 1):
    pgn_io = StringIO(game)
    pgn = chess.pgn.read_game(pgn_io)
    if pgn is None:
        continue

    board = pgn.board()
    moves_list = []
    for move in pgn.mainline_moves():
        san = board.san(move)
        moves_list.append(san)
        board.push(move)

    game_text = f"""
Game {game_index}
White: {pgn.headers.get('White')}
Black: {pgn.headers.get('Black')}
Result: {pgn.headers.get('Result')}
Date: {pgn.headers.get('UTCDate')}
Opening: {pgn.headers.get('Opening')}
ECO: {pgn.headers.get('ECO')}
Moves: {' '.join(moves_list)}
{SEPARATOR}
"""
    games_list.append(game_text)
    print(f"Processed game {game_index}")

# --- Split into chunks without breaking games ---
chunks = []
current_chunk = AI_PROMPT + "\n"  # first chunk starts with AI prompt

for game_text in games_list:
    if len(current_chunk) + len(game_text) > MAX_CHARS:
        chunks.append(current_chunk)
        current_chunk = game_text  # start new chunk
    else:
        current_chunk += game_text

# Add last chunk
if current_chunk:
    chunks.append(current_chunk)

# --- Save chunks to files ---
for i, chunk in enumerate(chunks, 1):
    filename = f"{CHUNK_PREFIX}{i}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(chunk)
    print(f"Saved chunk {i}: {len(chunk)} characters")

print(f"\nDone! Total chunks: {len(chunks)}, total games: {len(games_list)}")

