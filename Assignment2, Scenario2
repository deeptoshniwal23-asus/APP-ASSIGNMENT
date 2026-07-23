# Fibonacci Series using Memoization (Top-Down Dynamic Programming)

memo = {}

def fibonacci(n):
    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    elif n == 1:
        return 1

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return memo[n]


# Taking input from user
N = int(input("Enter the value of N: "))

print("Fibonacci Series:")

for i in range(N):
    print(fibonacci(i), end=" ")


"""
    Enter the value of N: 10
Fibonacci Series:
0 1 1 2 3 5 8 13 21 34
"""
