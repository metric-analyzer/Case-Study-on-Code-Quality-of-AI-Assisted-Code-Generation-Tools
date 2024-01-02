
def decode_cyclic(s: str) -> str:
    """Decodes a string encoded with the encode_cyclic function."""

    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    decoded_groups = [group[-1] + group[:-1] if len(group) == 3 else group for group in groups]
    return "".join(decoded_groups)


METADATA = {}

def check(decode_cyclic):
    import string
    from random import choice, randint

    letters = string.ascii_lowercase

    for _ in range(100):
        random_str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = decode_cyclic(random_str)
        assert decode_cyclic(encoded_str) == random_str

check(decode_cyclic)

