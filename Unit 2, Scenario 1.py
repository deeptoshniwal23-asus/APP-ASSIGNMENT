# Number of Ways to Make Change using Dynamic Programming

# Input coin denominations
coins = list(map(int, input("Enter the coin denominations: ").split()))

# Input target amount
amount = int(input("Enter the target amount: "))

# Create a DP array
dp = [0] * (amount + 1)

# There is one way to make amount 0
dp[0] = 1

# Calculate the number of ways
for coin in coins:
    for i in range(coin, amount + 1):
        dp[i] = dp[i] + dp[i - coin]

# Display the result
print("Total possible combinations:", dp[amount])





"""
Enter the coin denominations: 1 2 5 10
Enter the target amount: 20
Total possible combinations: 40
"""
