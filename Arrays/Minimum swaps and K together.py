'''
Minimum swaps required bring elements less equal K together


Time Complexity: O(n)
Reason:
  - Single pass through the array with two pointers (i and j)
  - Each element is visited exactly once
  - Swapping operation is O(1)
  - Total: O(n)

Space Complexity: O(1)
Reason: Only using constant extra space (i, j pointers)
        In-place swapping means no additional data structures needed
'''

def minimum_swaps_together(a, k):
    i=0
    for j in range(len(a)):
        if a[i]<k:
            i+=1
        elif a[j]<k:
            a[i],a[j]=a[j],a[i]
            i+=1
    print(a)

a=list(map(int,input("Enter the array elements: ").split()))
k=int(input("Enter the value of K: "))
minimum_swaps_together(a, k)