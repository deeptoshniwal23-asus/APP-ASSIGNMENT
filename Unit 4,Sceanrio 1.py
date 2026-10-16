
import numpy as np
import pandas as pd

# Create a NumPy array of electricity bills
bills = np.array([1500, 2500, 3500, 1800, 4200, 2900, 3200])

# Calculate statistics
print("Mean Bill:", np.mean(bills))
print("Median Bill:", np.median(bills))
print("Maximum Bill:", np.max(bills))
print("Minimum Bill:", np.min(bills))

# Create a Pandas DataFrame
data = {
    "Consumer ID": range(1, len(bills) + 1),
    "Bill Amount": bills
}

df = pd.DataFrame(data)

print("\nElectricity Bill Data:")
print(df)

# Display consumers whose bill exceeds ₹3000
print("\nConsumers with Bills Above Rs. 3000:")
print(df[df["Bill Amount"] > 3000])

Comment:-
Mean Bill: 2800.0
Median Bill: 2900.0
Maximum Bill: 4200
Minimum Bill: 1500

Electricity Bill Data:
   Consumer ID  Bill Amount
0            1         1500
1            2         2500
2            3         3500
3            4         1800
4            5         4200
5            6         2900
6            7         3200

Consumers with Bills Above Rs. 3000:
   Consumer ID  Bill Amount
2            3         3500
4            5         4200
6            7         3200
