'''
Find whether an array is a subset of another array

Time Complexity: O(n + m)
    - Creating set from arr1: O(n) where n is length of arr1
    - Iterating through arr2 and checking membership: O(m) where m is length of arr2
    - Each set lookup is O(1) on average
    - Total: O(n) + O(m) = O(n + m)

Space Complexity: O(n)
    - We create a set from arr1 which requires O(n) space
    - No other significant data structures are used
'''

def isSubset(arr1, arr2):
    set_a = set(arr1)
    for i in arr2:
        if i not in set_a:
            return False
    return True

a = list(map(int, input("Enter elements of first array separated by space: ").split()))
b = list(map(int, input("Enter elements of second array separated by space: ").split()))
print(isSubset(a, b))