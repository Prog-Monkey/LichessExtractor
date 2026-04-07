import tkinter as tk
from tkinter import scrolledtext, messagebox
import berserk
import chess.pgn
from io import StringIO

# --- Function to scrape games ---
def scrape_games():
    API_TOKEN = token_entry.get()
    USERNAME = username_entry.get()
    try:
        MAX_GAMES = int(max_games_entry.get())
        MAX_CHARS = int(max_chars_entry.get())
    except ValueError:
        messagebox.showerror("Error", "MAX_GAMES and MAX_CHARS must be integers")
        return
    CHUNK_PREFIX = prefix_entry.get()
    SEPARATOR = "\n---\n"

    AI_PROMPT = """I’m providing you with a collection of chess games played by a particular player...
Please analyze these games carefully and provide a comprehensive scouting report.
"""

    log_text.delete("1.0", tk.END)
    log_text.insert(tk.END, "Initializing Lichess client...\n")
    root.update()

    try:
        session = berserk.TokenSession(API_TOKEN)
        client = berserk.Client(session)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to initialize Lichess client: {e}")
        return

    games_list = []
    log_text.insert(tk.END, f"Fetching up to {MAX_GAMES} games for {USERNAME}...\n")
    root.update()

    try:
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
            log_text.insert(tk.END, f"Processed game {game_index}\n")
            log_text.see(tk.END)
            root.update()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch games: {e}")
        return

    # Split into chunks
    log_text.insert(tk.END, "Splitting into chunks...\n")
    root.update()
    chunks = []
    current_chunk = AI_PROMPT + "\n"

    for game_text in games_list:
        if len(current_chunk) + len(game_text) > MAX_CHARS:
            chunks.append(current_chunk)
            current_chunk = game_text
        else:
            current_chunk += game_text

    if current_chunk:
        chunks.append(current_chunk)

    # Save chunks
    for i, chunk in enumerate(chunks, 1):
        filename = f"{CHUNK_PREFIX}{i}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(chunk)
        log_text.insert(tk.END, f"Saved chunk {i}: {len(chunk)} characters\n")
        log_text.see(tk.END)
        root.update()

    log_text.insert(tk.END, f"\nDone! Total chunks: {len(chunks)}, total games: {len(games_list)}\n")
    root.update()
    messagebox.showinfo("Success", "All chunks saved successfully!")

# --- GUI ---
root = tk.Tk()
root.title("Lichess Game Scraper & Chunker")
root.geometry("700x500")

tk.Label(root, text="Lichess API Token:").grid(row=0, column=0, sticky="e")
token_entry = tk.Entry(root, width=50, show="*")
token_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Username:").grid(row=1, column=0, sticky="e")
username_entry = tk.Entry(root, width=50)
username_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Max Games:").grid(row=2, column=0, sticky="e")
max_games_entry = tk.Entry(root, width=50)
max_games_entry.grid(row=2, column=1, padx=5, pady=5)
max_games_entry.insert(0, "50")

tk.Label(root, text="Max Characters per Chunk:").grid(row=3, column=0, sticky="e")
max_chars_entry = tk.Entry(root, width=50)
max_chars_entry.grid(row=3, column=1, padx=5, pady=5)
max_chars_entry.insert(0, "15000")

tk.Label(root, text="Chunk File Prefix:").grid(row=4, column=0, sticky="e")
prefix_entry = tk.Entry(root, width=50)
prefix_entry.grid(row=4, column=1, padx=5, pady=5)
prefix_entry.insert(0, "reyaansh1814_chunk_")

start_button = tk.Button(root, text="Start Scraping", command=scrape_games)
start_button.grid(row=5, column=0, columnspan=2, pady=10)

log_text = scrolledtext.ScrolledText(root, width=80, height=20)
log_text.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

