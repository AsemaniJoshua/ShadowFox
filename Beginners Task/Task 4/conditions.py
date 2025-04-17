# Determining the BMI Category based on user input
# height = float(input("Enter the height in meters\n"))

# weight = float(input("Enter the weight in kilograms\n"))

# bmi = weight / height**2

# if bmi < 18.5:
#     print("Underweight")
# elif 18.5 <= bmi <= 24.9:
#     print("Normal weight")
# elif 25 <= bmi <= 29.9:
#     print("Overweight")
# else:
#     print("Obesity")

# Determing which country a city belongs to
# Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
# UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
# India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# # Accepting city input from the user and capitalizing each word
# city = input("Enter the name of a city\n").title().strip()

# # Checking if a city belongs to a country
# if city in Australia:
#     print(f"{city} is in Australia")
# elif city in UAE:
#     print(f"{city} is in UAE")
# elif city in India:
#     print(f"{city} is in India")
# else:
#     print(f"{city} is not in Australia, UAE or India")
    
# Checking if two cities is in the same country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the name of the first city\n").title().strip()
city2 = input("Enter the name of the second city\n").title().strip()

if city1 in Australia and city2 in Australia:
    print(f"Both cities are in Australia")
elif city1 in UAE and city2 in UAE:
    print(f"Both cities are in UAE")
elif city1 in India and city2 in India:
    print(f"Both cities are in India")
else:
    print(f"Both cities are not in the same country")