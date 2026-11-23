"""make.fun entry: the-joke-about-the-demo-20261123-0112

Writes one joke (one line) about working beside AI coding agents to
entry.txt as UTF-8. Deterministic: no network, no randomness, no clock.
"""
import os

TEXT = 'The agent filed the ticket, closed it "working as intended," and was right.'


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
