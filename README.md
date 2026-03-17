# Python Projects

A collection of Python projects, homework assignments, labs, and examples from an introductory computer science course (Fall 2023).

## Repository Structure

```
python_projects/
├── Projects/         # Projects
│   ├── Mancala/      # Mancala board game
│   ├── Tactego/      # Stratego-style strategy game
│   └── Retriever_Bell/ # Phone switchboard network simulator
├── Homeworks/        # Homework assignments (hw0–hw6)
├── Labs/             # Lab exercises (lab01–lab11)
└── Examples/         # Introductory Python examples
```

## Projects

### Mancala

A two-player implementation of the classic Mancala board game. Features an ASCII-rendered board, turn-based marble distribution, capture rules, and game-end detection.

### Tactego

A turn-based strategy board game inspired by Stratego. Supports configurable board sizes and piece types loaded from `.pieces` files, piece movement, combat resolution, and win-condition checking (capture the opponent's flag).

### Retriever Bell

A phone switchboard network simulator. Models switchboards (area codes) connected by trunk lines, supports phone number registration, and uses a recursive depth-first search to route calls between distant area codes. Network state can be saved and loaded via JSON.

## Homeworks

| Assignment | Topics |
|------------|--------|
| hw0 | Basic print statements and variables |
| hw1 | Math operations, strings, user input |
| hw2 | Conditionals, date logic, game logic |
| hw3 | Lists, algorithms, pattern detection |
| hw4 | Nested loops, string manipulation |
| hw5 | Recursion, nested lists, string patterns |
| hw6 | Recursion, list/tree depth, structural analysis |

## Labs

| Lab | Topics |
|-----|--------|
| lab01 | Basic I/O, calculator operations |
| lab02 | String manipulation, conditionals |
| lab05 | Functions and list operations |
| lab07 | List filtering and math operations |
| lab08 | List operations |
| lab09 | Recursive sequences |
| lab10 | String manipulation |
| lab11 | File I/O |

## Examples

Four short scripts demonstrating foundational Python concepts:

- **example-1.py** — If statements and string comparison
- **example-2.py** — Conditionals with modulo and string truthiness
- **example-3.py** — If-elif-else chains
- **example-4.py** — List access and iteration with filtering

## Requirements

- Python 3
- No external dependencies (standard library only: `json`, `random`)
