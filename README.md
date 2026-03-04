# AI Mini Assignments (Python) — Turing Test, CAPTCHA, and Uninformed Search

This repo contains three small Python programs built for AI fundamentals practice:
1) **Turing Test** — chats briefly and makes a rough “human vs bot” guess using simple heuristics.  
2) **CAPTCHA** — a quick challenge-response check (math-based) to block trivial bots.  
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

# Missionaries and Cannibals — Uninformed Search (BFS, DFS, IDDFS)

## Overview

This program solves the classic **Missionaries and Cannibals river-crossing problem** using three uninformed search algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)
- Iterative Deepening Depth First Search (IDDFS)

The goal is to safely move **three missionaries and three cannibals** from the left side of a river to the right side using a boat that can carry **a maximum of two people**.

The program models the puzzle as a **state-space search problem** and explores possible configurations until a valid solution is found.

It also compares how different uninformed search algorithms explore the problem.

---

# Problem Description

The problem follows these rules:

1. There are **3 missionaries and 3 cannibals** on one side of a river.
2. A boat can carry **one or two people** at a time.
3. The boat cannot move without at least **one person** in it.
4. On either side of the river, **cannibals cannot outnumber missionaries** when missionaries are present.
5. The goal is to move **everyone safely to the opposite side of the river**.

If a configuration violates these rules, it is considered an **invalid state** and is not explored.

---


This compact representation allows the program to easily track the state of the problem and generate new possible states during the search process.

---

# Program Architecture

The program models the problem as a **state-space search system**. It is divided into several logical components.

---

## State Validation

A validation function checks whether a generated state is valid and safe before it is explored further.

The validation step ensures that:

- The number of missionaries and cannibals remains within valid limits (0–3).
- Cannibals never outnumber missionaries on either side of the river when missionaries are present.

For example, the following state would be invalid:
(1,3,1)


because on the left side there is **1 missionary and 3 cannibals**, which would violate the safety constraint.

Invalid states are discarded and not added to the search process.

---

## Successor State Generation

From each state, the program generates possible **successor states** representing valid boat crossings.

The boat can carry one or two people, so the possible movements are:

- 1 missionary
- 2 missionaries
- 1 cannibal
- 2 cannibals
- 1 missionary and 1 cannibal

For each possible move:

1. The program updates the number of missionaries and cannibals on each side.
2. The boat position is switched to the opposite side.
3. The resulting state is checked using the validation function.

Only valid states are added to the search structure.

---

## Path Tracking

While searching, the program stores the **parent state** of each new state.  
This allows the program to reconstruct the full sequence of moves once the goal state is reached.

When the goal is found, the program traces back from the goal state to the initial state to produce the complete solution path.

---

# Search Algorithms Used

The program compares three uninformed search algorithms.

---

## Breadth First Search (BFS)

BFS explores the search space **level by level**.

This means it examines all states reachable in one move before exploring states that require two moves.

Characteristics:

- Uses a **queue** data structure.
- Guarantees the **shortest solution path**.
- Requires more memory because many states must be stored simultaneously.

---

## Depth First Search (DFS)

DFS explores one path **as deeply as possible** before backtracking.

Instead of exploring all nodes at one level, it follows one branch until it reaches a dead end.

Characteristics:

- Uses a **stack**.
- Requires less memory.
- Does **not guarantee the shortest solution**.

---

## Iterative Deepening Depth First Search (IDDFS)

IDDFS combines the advantages of BFS and DFS.

It repeatedly performs DFS with increasing depth limits:



---

# Algorithm Comparison

| Algorithm | Memory Usage | Finds Shortest Path | Exploration Style |
|----------|-------------|--------------------|------------------|
| BFS | High | Yes | Explores level-by-level |
| DFS | Low | No | Explores deep paths first |
| IDDFS | Low-Medium | Yes | Repeated depth-limited DFS |

This comparison shows how different uninformed search strategies explore the same state space in different ways.





