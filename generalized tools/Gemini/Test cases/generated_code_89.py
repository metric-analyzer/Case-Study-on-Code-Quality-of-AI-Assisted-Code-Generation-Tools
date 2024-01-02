
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


def check(encrypt):
    # Check some simple cases
    assert encrypt('hi') == 'lm', "Error"
    assert encrypt('asdfghjkl') == 'ewhjklnop', "Error"
    assert encrypt('gf') == 'kj', "Error"
    assert encrypt('et') == 'ix', "Error"
    assert encrypt('faewfawefaewg') == 'jeiajeaijeiak', "Error"
    assert encrypt('hellomyfriend') == 'lippsqcjvmirh', "Error"
    assert encrypt('dxzdlmnilfuhmilufhlihufnmlimnufhlimnufhfucufh') == 'hbdhpqrmpjylqmpyjlpmlyjrqpmqryjlpmqryjljygyjl', "Error"

    # Check some edge cases that are easy to work out by hand.
    assert encrypt('a') == 'e', "Error"

check(encrypt)
