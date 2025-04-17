# Function to accept two arguments: a number and a letter
# and print them in a formatted string
def numbers(number: int, letter: str):
    result = "Number: {0}, Letter: {1}".format(number, letter)
    print(result)
    
numbers(145, "o")

# Area of a Pond
pi = 3.14
radius = 80

area_of_circle = pi * radius**2
print("Area of the pond is: ", area_of_circle)

# Calculating the amount of water in the pond
# if 1.4 litres of water is needed to fill 1 square meter, then the water needed to fill the pond is:
water_needed = int(area_of_circle * 1.4)
print("Water needed to fill the pond is: ", water_needed, "meters")

# calculating your speed
# distance in meters
distance = 490
# time in seconds
time = 7*60

# speed in meters per second
speed = distance // time
print("Your speed is: ", speed, "meters per second")