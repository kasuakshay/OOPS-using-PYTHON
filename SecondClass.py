class House:

    # Count of Houses built
    houses_built = 0

    # private variable
    __build_cost = 0

    # Constructor for House class
    def __init__(self, windows, doors=3):
        self.windows = windows
        self.doors = doors
        House.houses_built += 1
        House.__build_cost = windows*500 + doors*1000

    # Print no. of doors
    def print_doors(self):
        print(f"Number of doors required : {self.doors}")

    # Print all variables
    def __str__(self):
        return f"The House has {self.windows} windows and {self.doors} doors. Total cost: {House.__build_cost}!"

    def __del__(self):
        print("House is demolished..!!")
        House.houses_built -= 1


# Create a house object
my_house = House(4, 2)
print(str(my_house))

# change value of variable
my_house.doors = 5
my_house.print_doors()

# Create number of houses and    check count
my_house2 = House(2, 2)
print(str(my_house2))
my_house3 = House(3, 2)
print(str(my_house3))
print(f"Houses built: {House.houses_built}")

# Delete house object
del my_house
print(f"Houses built: {House.houses_built}")

'''
Cannot access private variable from outside. 
print(House.__build_cost)

Error thrown:
AttributeError: type object 'House' has no attribute '__build_cost'
'''

