# Find all pairs on integer array whose sum is equal to given number
 
arr=list(map(int, input("Enter array elements separated by space: ").split()))
target_sum=int(input("Enter the target sum: "))

def find_pairs_with_sum(arr, target_sum):
    pairs=[]
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                pairs.append((arr[i], arr[j]))
    return pairs

result = find_pairs_with_sum(arr, target_sum)

if result:
    print("Pairs with sum", target_sum, "are:", result)
else:
    print("No pairs found with sum", target_sum)