import random

# Number of rolls
rolls = 20

count_6 = 0
count_1 = 0
two_6s_in_a_row = 0

previous_roll = None

# Simulate rolling the die
for i in range(rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")

    # Count number of 6s
    if roll == 6:
        count_6 += 1

    # Count number of 1s
    if roll == 1:
        count_1 += 1

    # Count two 6s in a row
    if roll == 6 and previous_roll == 6:
        two_6s_in_a_row += 1

    previous_roll = roll

# Print statistics
print("\nStatistics:")
print("Number of times rolled a 6:", count_6)
print("Number of times rolled a 1:", count_1)
print("Number of times rolled two 6s in a row:", two_6s_in_a_row)