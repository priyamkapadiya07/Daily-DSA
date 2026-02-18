'''
Method 1
'''
def isPalindrome(s):
    a=0
    b=len(s)-1
    while a<=b:
        if s[a]!=s[b]:
            return False
        a+=1
        b-=1
    return True

s=input("Enter a string: ")
if isPalindrome(s):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
# -------------------------------------------------------------------------------------------------------------------------
    
'''
Method 2
'''
def isPalindrome(s):
    return s == s[::-1]
input_str = input("Enter a string: ")
if isPalindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")