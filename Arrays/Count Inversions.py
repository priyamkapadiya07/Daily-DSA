# Count Inversions

a = [2, 3, 4, 5, 6]
c = 0

for i in range(len(a)-2):
    for j in range(i+1, len(a)-1):
        if a[i] > a[j]:
            c += 1
print(c)