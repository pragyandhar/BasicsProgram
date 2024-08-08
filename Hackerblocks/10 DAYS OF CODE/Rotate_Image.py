import numpy as np
# Read the size of the array
N = int(input())

# Initialize an empty 2D array
rows = []

# Read N lines of input
for _ in range(N):
    # Read each line and split the integers
    row = list(map(int, input().split()))
    # Append the row to the 2D array
    rows.append(row)

# Now, the 'array' variable contains the 2D array input by the user
array = np.array(rows)

#Transposing the array
t_arr = array.T


# Initialize an empty list to store reversed rows
reversed_rows = []

# Reverse each row of the transposed array
for row in t_arr:
    reversed_row = row[::-1]
    reversed_rows.append(reversed_row)

# Convert the list of reversed rows into a NumPy array
rev_arr = np.array(reversed_rows)

#Printing the array
for row in rev_arr:
    print(' '.join(map(str, row)))