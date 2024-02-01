# Question-15: Program that calculates the number of rectangular tiles required to cover a rectangular floor if the dimensions of the floor and the dimensions of a tile are entered by the user.

# INPUT SECTION
# For tiles
l = int(input("Enter the length of the tile(in sq. meters): "))
b = int(input("Enter the breadth of the tile(in sq. meters): "))
# For floor
L = int(input("Enter the length of the floor(in sq. meters): "))
B = int(input("Enter the breadth of the floor(in sq. meters): "))

# LOGIC SECTION: Find the area of the tiles and the floor and divide them to find out the number of tiles
Area_of_tiles = l*b
Area_of_floor = L*B
No_of_tiles = Area_of_floor/Area_of_tiles

# DISPLAY SECTION
print("The number of tiles required to fill", Area_of_tiles,
      "sq. meters of tiles in", Area_of_floor, "sq. meters of floor are", No_of_tiles)
