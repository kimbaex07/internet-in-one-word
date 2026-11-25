import os

WORD = "Doomscroll"

# Validation: the entry must be a single word of 1-30 characters,
# UTF-8 text with no control characters and no whitespace.
assert isinstance(WORD, str)
assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
assert WORD == WORD.strip(), "word must not have leading/trailing whitespace"
assert not any(ch.isspace() for ch in WORD), "word must be a single word"
assert not any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in WORD), (
    "word must not contain control characters"
)
WORD.encode("utf-8")  # raises if not valid UTF-8-encodable text

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(WORD)
