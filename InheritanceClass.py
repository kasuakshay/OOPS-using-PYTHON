from SecondClass import House


# Apartment is a child class of Parent class 'House'
class Apartments(House):

    # Method Overloading: Polymorphism
    def __init__(self, windows, doors=3, rooms=3):
        House.__init__(self, windows, doors)
        self.rooms = rooms

    # Method Overriding: Inheritance
    def print_doors(self):
        print(f"No. of Doors is : {self.doors * self.rooms}")

    # Method Overriding: Inheritance
    def __str__(self):
        return f"The Apartments has {self.rooms} house. " + super().__str__()


big_house = Apartments(10, 8, 2)
big_house.print_doors()
print(big_house)
