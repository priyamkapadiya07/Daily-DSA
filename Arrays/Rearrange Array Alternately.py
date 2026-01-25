# Rearrange the array in alternating positive and negative items with O(1) extra space

def rearrange_alternately(arr):
    i=0
    while i<len(arr):
        arr.insert(i,arr.pop())
        i+=2
    return arr

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
print(rearrange_alternately(sorted(arr)))