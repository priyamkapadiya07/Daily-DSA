
def isPalindrome(s):
    '''
    Method 1: Two-pointer technique to check palindrome.

    Time Complexity: O(n)
        - Compares characters from both ends, moving towards the center.
        - At most n/2 comparisons for a string of length n.
        - Each comparison is O(1), so total time is O(n).
    Space Complexity: O(1)
        - Uses only constant extra space for pointers (a, b), regardless of input size.
    '''
    a = 0
    b = len(s) - 1
    while a <= b:
        if s[a] != s[b]:
            return False
        a += 1
        b -= 1
    return True

s=input("Enter a string: ")
if isPalindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
# -------------------------------------------------------------------------------------------------------------------------

def isPalindrome(s):
    '''
    Method 2: Reverse and compare.

    Time Complexity: O(n)
        - s[::-1] creates a reversed copy of the string in O(n) time.
        - Comparing the original and reversed string also takes O(n) time.
        - Overall, time complexity is O(n).
    Space Complexity: O(n)
        - s[::-1] creates a new string of length n, so extra space required is O(n).
    '''
    return s == s[::-1]
input_str = input("Enter a string: ")
if isPalindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")