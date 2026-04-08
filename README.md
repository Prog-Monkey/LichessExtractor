# ♟️ **Lichess Extractor** ♟️

> *Your personal chess game analyzer! Scrape games from Lichess, organize them beautifully, and feed them to AI for genius-level insights.* 🚀

---

## ✨ **What's This All About?**

LichessExtractor is a **blazingly fast** Python tool that pulls your Lichess games and preps them for AI analysis. It extracts every detail—openings, moves, results—and chunks them perfectly for your AI model of choice!

---

## 🎯 **Features That Shine**

- ⚡ **Fetch games** directly from any Lichess player
- 🔍 **Extract rich metadata**:
  - White & Black player names
  - Game results & dates
  - Opening names & ECO codes
  - Complete move lists in Standard Algebraic Notation (SAN)
- 📦 **Smart chunking** – Splits games into manageable pieces (customizable size)
- 🤖 **AI-ready prompts** – Includes detailed analysis instructions in each chunk
- 💾 **Clean output** – Saves organized `.txt` files with your chosen prefix

---

## 📋 **What You Need**

- **Python 3.10+**
- [berserk](https://pypi.org/project/berserk/) – Lichess API client
- [python-chess](https://pypi.org/project/python-chess/) – PGN parsing magic

Install in seconds:
```bash
pip install berserk python-chess
```

---

## 🚀 **Quick Start**

### **Step 1: Get Your Lichess Token**
1. Head to [Lichess Tokens](https://lichess.org/account/oauth/token)
2. Create a new token with **"Read all your games"** permission
3. Copy that token! 🔐

### **Step 2: Configure the Script**
Open the script and set these values:
```python
API_TOKEN = "your_lichess_token_here"
USERNAME = "target_username_here"
MAX_GAMES = 50                 # How many games to grab
SEPARATOR = "\n---\n"          # Game separator
MAX_CHARS = 15000              # Characters per chunk
CHUNK_PREFIX = USERNAME+"_chunk_"  # Output file prefix
```

### **Step 3: Customize AI Prompt (Optional)**
```python
AI_PROMPT = """
Analyze these chess games for:
- Key strengths and weaknesses
- Opening tendencies
- Strategic patterns
- Personalized improvement tips
"""
```

### **Step 4: Run It! 🎯**
```bash
python gecko_assistant.py
```

---

## 📂 **Output Format**

Your extracted games will look like this:

```
Game 1
White: Magnus_Carlsen
Black: Fabiano_Caruna
Result: 1-0
Date: 2024.04.01
Opening: Sicilian Defense
ECO: B40
Moves: e4 c5 Nf3 d6 d4 cxd4 Nxd4 Nf6 Nc3 a6 ...
---
```

Files will be saved as:
- `USERNAME_chunk_1.txt`
- `USERNAME_chunk_2.txt`
- ...and so on! 📊

---

## 💡 **Pro Tips**

- 🔒 **Keep your token safe** – Never commit it to version control
- ⚙️ **Tune MAX_GAMES** for dataset size
- 📏 **Adjust MAX_CHARS** based on your AI model's input limits
- 🧠 **Perfect for** player analysis, opening prep, or feeding data to ML models

---

## 🎮 **Perfect For**

- 🔬 Player scouting and pattern analysis
- 🤖 Training AI models on chess strategies
- 📈 Personal chess improvement tracking
- 🏆 Tournament preparation

---

Made with ♟️ & ❤️ by **Prog-Monkey**