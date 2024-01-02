
def decode_cyclic(s: str) -> str:
    """Decodes a string encoded with the encode_cyclic function."""

    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    decoded_groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(decoded_groups)
