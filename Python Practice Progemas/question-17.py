# Question-17: Program to input the number of heads and feet in a farm and identify the number of chickens and goats in the farm. For example, if there are 340 heads and 1,060 feet, there are 150 chickens and 190 goats.

# INPUT SECTION
head = int(
    input("The number of Heads of the total number of animals in the farm: "))
legs = int(input("The number of Legs of the total number of animals in the farm: "))

# LOGIC SECTION: If no of hens are x and goats are y then total no of heads = x+y and total number of legs=2x+4y. Then, by solving the equations we can get the result
Total_chickens = ((4*head) - legs)/2
Total_goats = (legs - (2*head))/2

# DISPLAY SECTION
print("The number of chickens in the farm are:", Total_chickens)
print("The number of goats in the farm are:", Total_goats)
