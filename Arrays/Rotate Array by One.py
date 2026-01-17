# Write a program to cyclically rotate an array by one.

# Time Complexity: O(n*k) | Space Complexity: O(1)
# Reason: Each rotation uses insert/pop which is O(n). For k rotations total is O(n*k). No extra space used.

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
n=int(input("Enter no. of rotation you want: "))
no=n
while n>0:
    arr.insert(0,arr.pop())
    n-=1
print(f"After rotating array {no} times in clock-wise:",arr)