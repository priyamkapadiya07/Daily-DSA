# Find factorial of a large number

def factorial_large_number(num):
    result=1
    for i in range(1,num+1):
        result *= i
    return result

n = int(input("Enter a large number to find its factorial: "))
re = list(map(int, str(factorial_large_number(n))))
print(f"The factorial of {n} is: {re}")