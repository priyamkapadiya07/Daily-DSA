# Rearrange the array in alternating positive and negative items with O(1) extra space

"""
Time Complexity: O(n²)
Reason: arr.insert() operation is O(n) as it shifts elements, and this is done inside 
the while loop which runs approximately n/2 times, resulting in O(n) * O(n) = O(n²)

Space Complexity: O(1)
Reason: The array is modified in-place without using any additional data structures
"""

def rearrange_alternately(arr):
    i=0
    while i<len(arr):
        arr.insert(i,arr.pop())
        i+=2
    return arr

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print(rearrange_alternately(sorted(arr)))