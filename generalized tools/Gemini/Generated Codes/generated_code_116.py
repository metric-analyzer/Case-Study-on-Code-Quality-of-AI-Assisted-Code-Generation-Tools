def sort_array(arr):
 """
 Sorts an array of non-negative integers according to number of ones in their binary representation in ascending order.
 For similar number of ones, sort based on decimal value.

 Args:
     arr: A list of non-negative integers.

 Returns:
     A new list of integers sorted as described above.
 """

 def count_ones(n):
   """
   Counts the number of ones in the binary representation of a non-negative integer.

   Args:
       n: A non-negative integer.

   Returns:
       The number of ones in the binary representation of n.
   """
   count = 0
   while n:
     count += n & 1
     n >>= 1
   return count

 # Sort the array using a custom key function that considers both the number of ones and the decimal value.
 return sorted(arr, key=lambda x: (count_ones(x), x))

# Example usage
arr = [1, 5, 2, 3, 4]
sorted_arr = sort_array(arr)
print(sorted_arr)  # Output: [1, 2, 4, 3, 5]
