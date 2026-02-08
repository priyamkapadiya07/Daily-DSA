# Palindromic Array

arr = [121, 131, 20]

for i in arr:
    s = str(i)
    l=0
    r=len(s)-1
    while l<r:
        if s[l]!=s[r]:
            print("Not Palindromic Array")
            exit()
        l+=1
        r-=1
print("Palindromic Array")