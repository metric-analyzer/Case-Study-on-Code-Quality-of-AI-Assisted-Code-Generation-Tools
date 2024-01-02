def maximum(arr, k):
 """
 Finds the k largest elements in an array and returns them as a sorted list.

 Args:
     arr: The input array of integers.
     k: The number of largest elements to find.

 Returns:
     A sorted list containing the k largest elements in the array.
 """

 # Use a min-heap to efficiently find the k largest elements
 import heapq
 heap = []
 for num in arr:
   heapq.heappush(heap, -num)  # Negate elements to turn max-heap into min-heap
   if len(heap) > k:
     heapq.heappop(heap)  # Remove smallest element if heap exceeds size k

 # Convert the heap back to a sorted list of largest elements
 return sorted([-x for x in heap])

# Example usage
arr = [-3, -4, 5]
k = 3
largest_k = maximum(arr, k)
print(f"Largest {k} elements in {arr}: {largest_k}")


def check(maximum):
    # Check some simple cases
    assert maximum([-3, -4, 5], 3) == [-4, -3, 5], "Test 1"
    assert maximum([4, -4, 4], 2) == [4, 4], "Test 2"
    assert maximum([-3, 2, 1, 2, -1, -2, 1], 1) == [2], "Test 3"
    assert maximum([123, -123, 20, 0 , 1, 2, -3], 3) == [2, 20, 123], "Test 4"
    assert maximum([-123, 20, 0 , 1, 2, -3], 4) == [0, 1, 2, 20], "Test 5"
    assert maximum([5, 15, 0, 3, -13, -8, 0], 7) == [-13, -8, 0, 0, 3, 5, 15], "Test 6"
    assert maximum([-1, 0, 2, 5, 3, -10], 2) == [3, 5], "Test 7"
    assert maximum([1, 0, 5, -7], 1) == [5], "Test 8"
    assert maximum([4, -4], 2) == [-4, 4], "Test 9"
    assert maximum([-10, 10], 2) == [-10, 10], "Test 10"

    # Check the function
    check(maximum)
