
def decode_shift(s: str) -> str:
    """Decodes a string encoded with encode_shift by shifting characters back by 5."""

    return "".join([chr(((ord(ch) - 5 - ord("a") + 26) % 26) + ord("a")) for ch in s])
