'''
Find whether an array is a subset of another array
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