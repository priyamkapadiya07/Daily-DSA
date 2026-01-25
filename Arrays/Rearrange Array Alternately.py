# Rearrange the array in alternating positive and negative items with O(1) extra space

def rearrange_alternately(arr):
    i=0
    while i<len(arr):
        arr.insert(i,arr.pop())
        i+=2
    return arr

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print(rearrange_alternately(sorted(arr)))