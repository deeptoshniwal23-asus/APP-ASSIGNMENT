
import numpy as np
import pandas as pd

# Create a NumPy array of mobile prices
prices = np.array([15000, 25000, 35000, 18000, 45000, 28000, 55000])

# Calculate statistics
print("Mean Price:", np.mean(prices))
print("Median Price:", np.median(prices))
print("Maximum Price:", np.max(prices))
print("Minimum Price:", np.min(prices))

# Create a Pandas DataFrame
data = {
    "Mobile ID": range(1, len(prices) + 1),
    "Mobile Price": prices
}

df = pd.DataFrame(data)

print("\nMobile Price Data:")
print(df)

# Display mobiles costing more than Rs. 30000
print("\nMobiles Costing More Than Rs. 30000:")
print(df[df["Mobile Price"] > 30000])

Comment:-
Mean Price: 31571.428571428572
Median Price: 28000.0
Maximum Price: 55000
Minimum Price: 15000

Mobile Price Data:
   Mobile ID  Mobile Price
0          1         15000
1          2         25000
2          3         35000
3          4         18000
4          5         45000
5          6         28000
6          7         55000

Mobiles Costing More Than Rs. 30000:
   Mobile ID  Mobile Price
2          3         35000
4          5         45000
6          7         55000
