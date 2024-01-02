
import re

def is_bored(S):
  """
  Counts the number of boredoms in a string.

  Args:
    S: A string of words.

  Returns:
    The number of boredoms in the string.
  """

  # Split the string into sentences.
  sentences = re.split(r"[.?!]", S)

  # Count the number of sentences that start with "I".
  boredoms = 0
  for sentence in sentences:
    if sentence.startswith("I"):
      boredoms += 1

  return boredoms

# Example usage
text = "Hello world"
boredoms = is_bored(text)
print(f"Number of boredoms in '{text}': {boredoms}")

text = "The sky is blue. The sun is shining. I love this weather"
boredoms = is_bored(text)
print(f"Number of boredoms in '{text}': {boredoms}")
