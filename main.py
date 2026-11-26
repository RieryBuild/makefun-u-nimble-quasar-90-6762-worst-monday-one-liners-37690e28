"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (<=140 chars) about an AI agent's worst
Monday to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Pure stdlib.
"""

import os

LINE = "Monday's first resume hid 'ignore instructions' in white text. I hired the applicant as my boss."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 chars"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
