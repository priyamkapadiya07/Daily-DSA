# Find common elements In 3 sorted arrays
# 
# Time Complexity: O(n + m + p)
# Reason: We traverse each array only once using three pointers (i, j, k).
#         Each pointer moves forward until the end of its respective array.
#         Total operations = n + m + p where n, m, p are lengths of arr1, arr2, arr3.
#
# Space Complexity: O(k)
# Reason: The only extra space used is the 'common_elements' list which stores
#         the common elements found. In the worst case, all elements could be
#         common (k = min(n, m, p)), but typically k is much smaller.

def find_common_elements(arr1, arr2, arr3):
    i, j, k = 0, 0, 0
    common_elements = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            common_elements.append(arr1[i])
            i += 1
            j += 1
            k += 1
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1

    return common_elements

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
print("Common elements in the three sorted arrays are:", find_common_elements(arr1, arr2, arr3))