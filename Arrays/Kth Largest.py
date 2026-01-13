# Kth Largest Element in an Array
def kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
k = int(input("Enter the value of k: "))

print(f"The {k}th largest element is:", kth_largest(arr, k))