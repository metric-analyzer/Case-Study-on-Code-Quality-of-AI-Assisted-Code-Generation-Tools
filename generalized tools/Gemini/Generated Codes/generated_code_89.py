
def encrypt(s):
  """Encrypts a string by rotating the alphabet by 4 positions.

  Args:
    s: The string to encrypt.

  Returns:
    The encrypted string.
  """

  alphabet = "abcdefghijklmnopqrstuvwxyz"
  shifted_alphabet = alphabet[4:] + alphabet[:4]
  table = str.maketrans(alphabet, shifted_alphabet)
  return s.translate(table)
