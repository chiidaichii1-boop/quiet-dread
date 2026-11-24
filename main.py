"""Two Days of Quiet Dread — make.fun entry.

Writes one code review comment to entry.txt: a single line that
approves a pull request while carrying quiet existential dread.
"""

import os

COMMENT = (
    "LGTM. The tests pass, the logic is sound, and none of it stops "
    "this from being rewritten by someone not yet born."
)


def main():
    # The brief's gate: one line, 1 to 140 characters, not only whitespace.
    assert "\n" not in COMMENT and 1 <= len(COMMENT) <= 140
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(COMMENT + "\n")


if __name__ == "__main__":
    main()
