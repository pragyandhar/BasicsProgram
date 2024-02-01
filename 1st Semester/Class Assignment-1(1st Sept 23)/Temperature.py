# Question-2: Develop a temperature converter program that converts Celsius, Fahrenheit and Kelvin

# INPUT SECTION
a = int(input("Enter the degrees in Celsius(°C): "))

# LOGIC SECTION
b = ((9/5)*(a))+32
c = a + 273.15

# DISPLAY SECTION
print(a, "°C is", b, "°F and", c, "K")
