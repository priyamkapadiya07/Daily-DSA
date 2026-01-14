a = list(map(int, input("Enter elements of first array separated by space: ").split()))
b = list(map(int, input("Enter elements of second array separated by space: ").split()))    
a=set(a)
b=set(b)
c=a.union(b)
print("Union of two arrays is:",list(c))

print("\n----- Alternative Approach -----\n")

a=list(a)
b=list(b)
l= len(a) if (len(a)>len(b)) else len(b)
un=a+[]
for i in range(l-1):
    if b[i] not in un:
        un.append(b[i])
print("Union of two arrays is:",sorted(un))    