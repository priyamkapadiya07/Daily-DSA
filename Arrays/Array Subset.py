'''
Find whether an array is a subset of another array
'''


def isSubset(arr1, arr2):
    set_a = set(arr1)
    for i in arr2:
        if i not in set_a:
            return False
    return True

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]
print(isSubset(a, b))