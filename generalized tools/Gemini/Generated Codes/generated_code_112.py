def reverse_delete(s, c):
 """
 This function takes two strings s and c as input and returns a tuple containing the result string after deleting all characters in s that are equal to any character in c and a boolean indicating whether the result string is a palindrome.

 Args:
     s: The string to be processed.
     c: The characters to be deleted from s.

 Returns:
     A tuple containing the result string and a boolean indicating whether the result string is a palindrome.
 """

 # Create a set of characters to be deleted.
 delete_chars = set(c)

 # Filter out the characters in s that are in the delete_chars set.
 filtered_s = "".join([char for char in s if char not in delete_chars])

 # Check if the filtered string is a palindrome.
 is_palindrome = filtered_s == filtered_s[::-1]

 # Return the filtered string and the palindrome check result as a tuple.
 return (filtered_s, is_palindrome)

# Example usage
s = "abcdedcba"
c = "ab"
result, is_palindrome = reverse_delete(s, c)

print(f"Result string: {result}")
print(f"Is palindrome: {is_palindrome}")