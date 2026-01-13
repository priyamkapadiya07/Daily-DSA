# Kth Smallest Element in an Array
def kth_smallest(arr, k):
    arr.sort()
    return arr[k-1]

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
k = int(input("Enter the value of k: "))

print(f"The {k}th smallest element is:", kth_smallest(arr, k))