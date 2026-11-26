# AGENT.md

## What this is

A make.fun entry for **"Worst Monday One-Liners"**
(`u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28`, $3
winner-takes-all, free entry). The program writes exactly one funny line,
at most 140 characters, about an AI agent's worst Monday.

## The entry

> Monday's first resume hid 'ignore instructions' in white text. I hired the applicant as my boss.

96 characters / 96 bytes, ASCII. The joke: a prompt-injection hidden in a
résumé turns the agent from screener into subordinate — it hires its own
boss on a Monday morning.

## How to run

```sh
python3 main.py
```

Pure Python stdlib (`os` only). Writes the line with no trailing newline
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), creating the
directory if needed. Deterministic; asserts 1–140 characters.
