'''Trapping Rain water problem'''

a=[3,0,1,0,4,0,2]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        a[i+1]=a[i]
print(a)