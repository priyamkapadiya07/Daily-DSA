ch=int(input("Enter (1 for string and 2 for array) reverse: "))

if ch==1:
    s=input("Enter a string: ")
    print("Reversed string:", s[::-1])
elif ch==2:
    arr=input("Enter array elements separated by space: ").split()
    # arr.reverse()
    for i in range(len(arr)-1,0,-1):
        print(arr[i],end=" ")
    print(arr[0])