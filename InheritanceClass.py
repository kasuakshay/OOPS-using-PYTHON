from SecondClass import House


class Apartments(House):

    def __init__(self, windows, doors=3, rooms=3):
        House.__init__(self, windows, doors)
        self.rooms = rooms

    def print_doors(self):
        print(f"No. of Doors is : {self.doors * self.rooms}")

    # Print all variables
    def __str__(self):
        return f"The Apartments has {self.rooms} containing {self.windows} windows and {self.doors} doors. "


big_house = Apartments(10, 8, 2)
big_house.print_doors()
print(big_house)
