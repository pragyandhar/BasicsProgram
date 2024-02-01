# INPUT SECTION
a = int(input("Enter the position: "))
b = 0
c = 0
d = 0
# LOGIC SECTION-1
for i in range(b, 100):
    if i%3 != 0 and i%10 != 3:
        b = b+1
        if b == a:
            print("The number of Hewlett-Packard Series is: ", i)
# LOGIC SECTION-2
while True:
    d = d+1
    if d%3 != 0 and d%10 != 3:
        c = c+1
        if c == a:
            print("The number of Hewlett-Packard Series is: ", d)
            break
        