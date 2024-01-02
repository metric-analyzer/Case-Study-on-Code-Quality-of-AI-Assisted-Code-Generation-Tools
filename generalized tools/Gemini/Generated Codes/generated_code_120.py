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
