# Create inheritance using MobilePhone as base class and Apple &
# Samsung as child class
# 1. The base class should have properties:
# 1. ScreenType = Touch Screen
# 2. NetworkType = 4G/5G
# 3. DualSim = True or False
# 4. FrontCamera = (5MP/8MP/12MP/16MP)
# 5. rearCamera = (8MP/12MP/16MP/32MP/48MP)
# 6. RAM = (2GB/3GB/4GB)
# 7. Storage = (16GB/32GB/64GB)
# 2. Create basic mobile phone functionalities in the classes like:
# make_call, recieve_call, take_a_picture, etc.
# 3. Use super() constructor for calling parent class’s constructor
# 4. Make some objects of Apple class with different properties
# 5. Make some objects of Samsung class with different properties

class Mobile:
    def __init__(self):
        self.ScreenType = "Touch Screen"
        self.NetworkType = "4G/5G"
        self.DualSim = True
        self.FrontCamera = "5MP/8MP/12MP/16MP"
        self.rearCamera = "8MP/12MP/16MP/32MP/48MP"
        self.RAM = "2GB/3GB/4GB"
        self.Storage = "16GB/32GB/64GB"
        
    # Mobile Phone Functionalities
    def make_call(self):
        print("Mobile Phone can be used to make calls")
        
    
    def receive_call(self):
        print("Mobile can be used to receive calls")
        
    def take_picture(self):
        print("Mobile Phone can be used to take a picture")
        
        
        
# class Apple
        
class Apple(Mobile):
    def __init__(self):
        super().__init__()
        self.DualSim = False
        self.NetworkType = "4G"
        self.RAM = "4GB"
        self.Storage = "64GB"
        
        
    # Apple Phone Functionalities
    def make_call(self):
        print("Apple Phone can be used to make calls")
        
    
    def receive_call(self):
        print("Apple can be used to receive calls")
        
    def take_picture(self):
        print("Apple Phone can be used to take a picture")
        
    
        
        
        
# Class Samsung
class Samsung(Mobile):
    def __init__(self):
        super().__init__()
        self.DualSim = True
        self.NetworkType = "5G"
        self.RAM = "4GB"
        self.Storage = "64GB"
        
        
    # Samsung Phone Functionalities
    def make_call(self):
        print("Samsung Phone can be used to make calls")
        
    
    def receive_call(self):
        print("Samsung can be used to receive calls")
        
    def take_picture(self):
        print("Samsung Phone can be used to take a picture")
        
        

# Creating Apple Object 
myApple_Phone = Apple()
print(myApple_Phone.DualSim)
myApple_Phone.take_picture()
myApple_Phone.make_call()

# Creating Samsung Object
mySamsung_Phone = Samsung()
print(mySamsung_Phone.DualSim)
mySamsung_Phone.make_call()
mySamsung_Phone.receive_call()
mySamsung_Phone.take_picture()


    