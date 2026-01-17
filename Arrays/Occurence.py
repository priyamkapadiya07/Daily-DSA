# from given array if user enter occurence then find element which more than or equal to occurence

# Time Complexity: O(n) | Space Complexity: O(n)
# Reason: Single pass to build dictionary. Dictionary stores all unique elements. Result list contains filtered elements.
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
occurence = int(input("Enter the occurence value: "))
d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1
    
result = [key for key, value in d.items() if value >= occurence]
print("Elements with occurence more than or equal to", occurence, "are:", result)
