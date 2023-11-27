import os
import random

# Create a 5x5 matrix with random values between 0 and 50
data = [[random.randint(0, 50) for _ in range(32)] for _ in range(32)]

# Specify the file path within the 'inputs' folder
file_path = os.path.join('vault_inputs', 'custom3.txt')

# Ensure the 'inputs' folder exists
os.makedirs('inputs', exist_ok=True)

# Write the data to custom.txt in the 'inputs' folder
with open(file_path, "w") as file:
    for row in data:
        file.write(','.join(map(str, row)) + '\n')

print(f"Random data has been written to {file_path}.")
