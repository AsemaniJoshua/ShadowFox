# Creating Instances of the class
from Classes_Object import Avengers

# Creating a list of dictionary to store the details of the Avengers from this list super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]
super_heroes = [
    {"name": "Captain America", "Age": 35, "Gender": "Male", "Super_Power": "Super strength", "Weapon": "Shield"},
    {"name": "Iron Man", "Age": 45, "Gender": "Male", "Super_Power": "Technology", "Weapon": "Amor"},
    {"name": "Black Widow", "Age": 30, "Gender": "Female", "Super_Power": "superhuman", "Weapon": "Batons"},
    {"name": "Hulk", "Age": 40, "Gender": "Male", "Super_Power": "Unlimited Strength", "Weapon": ""},
    {"name": "Thor", "Age": 50, "Gender": "Male", "Super_Power": "Super Energy", "Weapon": "Mjölnir"},
    {"name": "Hawkeye", "Age": 35, "Gender": "Male", "Super_Power": "Fighting Skills", "Weapon": "Bow and Arrows"},
]

# Creating a list to store the instances of the class
avengers = []
# Creating instances of the class and appending them to the list
for hero in super_heroes:
    avenger = Avengers(hero["name"], hero["Age"], hero["Gender"], hero["Super_Power"], hero["Weapon"])
    avengers.append(avenger)
# Printing the details of the avengers
for avenger in avengers:
    print(avenger.get_info())
    print(f"Is {avenger.name} a leader? {'Yes' if avenger.is_leader() else 'No'}")
    print("-" * 50)
