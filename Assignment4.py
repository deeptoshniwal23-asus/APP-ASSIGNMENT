# Fibonacci using Memoization (Top-Down Approach)

def fib_memo(num, cache={}):
    if num in cache:
        return cache[num]

    if num == 0:
        return 0
    if num == 1:
        return 1

    cache[num] = fib_memo(num - 1, cache) + fib_memo(num - 2, cache)
    return cache[num]


# Main Program
n = int(input("Enter the position (n): "))
result = fib_memo(n)

print("The", n, "th Fibonacci number is:", result)


"""

Enter the position (n): 10
The 10 th Fibonacci number is: 55

"""




# Fibonacci using Tabulation (Bottom-Up Approach)

def fib_tab(num):
    if num == 0:
        return 0
    if num == 1:
        return 1

    fib = [0] * (num + 1)
    fib[0] = 0
    fib[1] = 1

    for index in range(2, num + 1):
        fib[index] = fib[index - 1] + fib[index - 2]

    return fib[num]


# Main Program
n = int(input("Enter the position (n): "))
answer = fib_tab(n)

print("The", n, "th Fibonacci number is:", answer)



"""

Enter the position (n): 10
The 10 th Fibonacci number is: 55

"""
