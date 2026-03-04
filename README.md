###AI ASSIGNMENT-2 (INDIVIDUAL ASSIGNMENTS)

# AI Mini Assignments (Python) — Turing Test, CAPTCHA, and Uninformed Search

This repo contains three small Python programs built for AI fundamentals practice:
1) **Turing Test ** — chats briefly and makes a rough “human vs bot” guess using simple heuristics.  
2) **CAPTCHA ** — a quick challenge-response check (math-based) to block trivial bots.  
3) **Missionaries & Cannibals (Uninformed Search)** — solves the classic river-crossing problem using **BFS, DFS, and IDDFS** and compares them.


---

## Requirements

- **Python 3.8+**
- No external libraries needed (only Python standard library)

---


## How to Run

### 1) ALL
```bash
python turing_test.py
python captcha.py
python uninformedsearch.py
```



---

# 1. Turing Test Simulation

The Turing Test program simulates a short conversation with the user. It asks a few questions and evaluates the responses to estimate whether the user behaves more like a human or a bot.

The evaluation is based on simple factors such as response time, message length, and certain language patterns.

At the end of the interaction, the program prints a prediction indicating whether the responses appear human-like.

## Architecture

The code is organized into three main parts:

**1. Input / Interaction Layer**

The program asks a sequence of questions and collects user responses through the terminal.

**2. Response Analysis**

Each response is evaluated using simple rules such as:
- response time
- text length
- punctuation or formatting patterns

A small scoring function assigns points based on these characteristics.

**3. Decision Logic**

The scores from all responses are combined and the program prints a final verdict:
- Human
- Bot
- Uncertain

---

# 2. CAPTCHA Verification

## What the Code Does

The CAPTCHA program verifies that the user is human by presenting a simple challenge.

The program randomly generates a small arithmetic problem (for example `12 + 7`) and asks the user to compute the answer.

If the user enters the correct result, the verification passes.

## Architecture

The CAPTCHA program consists of three main steps:

**1. Challenge Generation**

Random numbers and a mathematical operator are generated using Python's random module.

**2. User Interaction**

The generated challenge is displayed to the user and input is collected from the terminal.

**3. Verification**

The program compares the user’s input with the correct answer and prints either a success or failure message.

---

# 3. Missionaries and Cannibals – Search Algorithms

## What the Code Does

This program solves the classic Missionaries and Cannibals river-crossing problem using three uninformed search algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Iterative Deepening Depth First Search (IDDFS)

The goal is to move all missionaries and cannibals from the left side of the river to the right side without violating the safety rules.

The program also compares the algorithms by printing the solution path and search statistics.

## Architecture

The search program is structured into several components:

**1. State Representation**

Each state represents the current configuration of the problem:



