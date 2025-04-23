# Creating a class of Avengers
class Avengers:
    # Constructor
    def __init__(self, name, Age, Gender, Super_Power, Weapon):
        self.name = name
        self.Super_Power = Super_Power
        self.Age = Age
        self.Gender = Gender
        self.Weapon = Weapon

    # Function to print the details
    def get_info(self):
        return (f"Name: {self.name}\nAge: {self.Age}\nGender: {self.Gender}\nSuper Power: {self.Super_Power}\nWeapon: {self.Weapon}")
    
    # Function to check if the Super Hero is a leader
    def is_leader(self):
        return self.name.lower() == "captain america"
        
    
        
        
