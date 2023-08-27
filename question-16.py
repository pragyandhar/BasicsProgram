# Question-16: Program to input the number of overs in a Cricket match and output the maximum runs a player can score in the match. Assume that there are no extra runs or NO balls in the match played. For example, in a 50 over match, the maximum runs scored are 1653.

# INPUT SECTION
overs = int(input("Enter the number of overs in a cricket match: "))

# LOGIC SECTION: In one over the batsman should hit 6 on 5 balls and run a maximum runs of 3 to keep the strike to himself So, he can score 33 runs at max in one over till (x-1)th over. In the last over he can hit a six at the last ball so a maximum of 36 runs in the last over.
total_runs = (33*(overs-1)) + 36

# DISPLAY SECTION
print("The total runs scored by the batsman in a",
      overs, "over match is:", total_runs)
