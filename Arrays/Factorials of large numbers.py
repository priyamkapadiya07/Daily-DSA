# Find factorial of a large number
#
# Time Complexity: O(n)
# Reason: The loop iterates from 1 to n, performing one multiplication operation 
#         in each iteration. Hence, total operations = n.
#
# Space Complexity: O(n) 
# Reason: The result grows exponentially with n. A factorial of n has approximately
#         n*log10(n) digits, requiring O(n) space to store the large number as a string.
#         Python handles this natively with arbitrary precision integers.

def factorial_large_number(num):
    result=1
    for i in range(1,num+1):
        result *= i
    return result

n = int(input("Enter a large number to find its factorial: "))
re = list(map(int, str(factorial_large_number(n))))
print(f"The factorial of {n} is: {re}")