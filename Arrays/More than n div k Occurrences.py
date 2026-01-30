"""
Given an array of size n and a number k, find all elements that appear more than "n/k" times.

Time Complexity: O(n)
    - First loop iterates through all n elements: O(n)
    - Second loop iterates through unique elements (at most n): O(n)
    - Total: O(n)

Space Complexity: O(n)
    - Dictionary stores at most n unique elements in worst case (all elements are unique)
    - Uses O(n) space for the dictionary
"""

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
k = int(input("Enter the value of k: "))

d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1

res = 0
for key in d:
    if d[key] > len(arr) // k:
        res += 1

print(res)