# Merge 2 sorted arrays without using Extra space.

a = [2, 4, 7, 10]
b = [2, 3]
# Approach: Combine both arrays and sort them.
print(sorted(a+b))

# Optimal Approach: Start from the end of first array and beginning of second array.
def merge_array(a,b):
    i=len(a)-1
    j=0
    while i>=0 and j<len(b):
        if a[i]>b[j]:
            a[i],b[j]=b[j],a[i]
            i-=1
            j+=1
        else:
            break
    a.sort()
    b.sort()
    return a,b
print(merge_array(a,b))