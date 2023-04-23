class Person:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        

    def describe(self):
        return self.name + ", " + self.address +", " + self.phone   