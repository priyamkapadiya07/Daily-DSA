'''
Docstring for Arrays.Addition of array
'''
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
l3 = [0] * max(len(l1), len(l2))
carry = 0
for i in range(len(l3)):
    if i<len(l1):
        carry += l1[i]
    if i<len(l2):
        carry += l2[i]
    l3[i] = carry % 10
    carry //= 10
if carry:
    l3.append(carry)
print(l3)