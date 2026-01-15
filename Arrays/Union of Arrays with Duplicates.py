# Find the Union and Intersection of the two sorted arrays.

n= int(input("Enter 1 for Union and 2 for Intersection of two arrays: "))

a = list(map(int, input("Enter elements of first array separated by space: ").split()))
b = list(map(int, input("Enter elements of second array separated by space: ").split()))    
a=set(a)
b=set(b)

if n==1:
    c=a.union(b)
    print("Union of two arrays is:",list(c))

    print("\n----- Alternative Approach -----\n")

    a=list(a)
    b=list(b)
    l= len(a) if (len(a)<len(b)) else len(b)
    un=a+[]
    for i in range(l-1):
        if b[i] not in un:
            un.append(b[i])
    print("Union of two arrays is:",sorted(un))
    
elif n==2:
    c=a.intersection(b)
    print("Intersection of two arrays is:",list(c))
    
    print("\n----- Alternative Approach -----\n")
    
    a=list(a)
    b=list(b)
    l= len(a) if (len(a)>len(b)) else len(b)
    inter=[]
    if len(a)>len(b):
        for i in range(l-1):
            if a[i] in b:
                inter.append(a[i])
    else:
        for i in range(l-1):
            if b[i] in a:
                inter.append(b[i])
    print("Intersection of two arrays is:",sorted(inter))
    