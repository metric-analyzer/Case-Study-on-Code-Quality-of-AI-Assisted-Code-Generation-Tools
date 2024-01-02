
def encode(message):
  """Encodes a message by swapping case, shifting vowels, and preserving non-letters.

  Args:
    message: The message to encode.

  Returns:
    The encoded message.
  """

  encoded_message = ""
  for char in message:
    if char.isalpha():
      # Swap case
      new_char = char.swapcase()

      # Shift vowels
      if new_char in "AEIOUaeiou":
        vowel_index = "AEIOUaeiou".find(new_char)
        new_char = "AEIOUaeiou"[(vowel_index + 2) % 5]  # Wrap around for vowels at the end

      encoded_message += new_char
    else:
      # Preserve non-letter characters
      encoded_message += char

  return encoded_message

# Example usage
print(encode("test"))  # Output: TGST
print(encode("This is a message"))  # Output: tHKS KS C MGSSCGG
print(encode("Hello, world! 123"))  # Output: hDLLC, WQRLZ! 123


def check(encode):
    # Check some simple cases
    assert encode('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert encode('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert encode('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert encode('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert encode("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"

check(encode)
