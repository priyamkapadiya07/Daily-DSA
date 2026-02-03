'''Trapping Rain water problem'''
a=[3,0,1,0,4,0,2]
l=a
r=a
# left max
for i in range(len(a)-1):
    if l[i]>l[i+1]:
        l[i+1]=l[i]
print(l)

# right max
for i in range(len(r)-1,0,-1):
    if r[i-1]<r[i]:
        r[i-1]=r[i]
print(r)