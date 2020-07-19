class House:

    # Constructor for House class
    def __init__(self, windows, doors=3):
        self.windows = windows
        self.doors = doors

    # Print no. of doors
    def print_doors(self):
        print(f"Number of doors required : {self.doors}")

    # Print all variables
    def print_house(self):
        print(f"The House has {self.windows} windows and {self.doors} doors.!")


my_house = House(4, 2)
my_house.print_house()

my_house.doors = 5
my_house.print_doors()
