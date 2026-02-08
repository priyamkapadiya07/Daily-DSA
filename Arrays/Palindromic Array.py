# Palindromic Array
# Check whether all integers in the array are palindromic (digits read the same
# forward and backward).
#
# Time complexity: O(n * k)
# Reason: Let n be the number of elements in the array and k be the average
# number of digits per element. For each element we convert it to a string
# (O(k)) and run a two-pointer comparison which checks up to O(k) characters.
#
# Space complexity: O(1)
# Reason: The algorithm uses a constant number of scalar variables
# (`original`, `reversed_num`, `digit`, etc.) and performs the reversal
# in-place mathematically. No additional data structures proportional to
# n or the number of digits (k) are allocated.

arr = [121, 131, 202, 12321]

for num in arr:
    if num < 0:
        print("Not Palindromic Array")
        exit()
        
    original = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = (reversed_num * 10) + digit
        num //= 10
    
    if original != reversed_num:
        print("Not Palindromic Array")
        exit()

print("Palindromic Array")