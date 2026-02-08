# Palindromic Array
# Check whether all integers in the array are palindromic (digits read the same
# forward and backward).
#
# Time complexity: O(n * k)
# Reason: Let n be the number of elements in the array and k be the average
# number of digits per element. For each element we convert it to a string
# (O(k)) and run a two-pointer comparison which checks up to O(k) characters.
#
# Space complexity: O(1) additional space (or O(k) if accounting for the
# temporary string created by `str()`)
# Reason: The algorithm only uses a few scalar variables; converting a number
# to a string requires O(k) space but we do not allocate extra structures that
# scale with n.

arr = [121, 131, 20]

for i in arr:
    s = str(i)
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            print("Not Palindromic Array")
            exit()
        l += 1
        r -= 1

print("Palindromic Array")