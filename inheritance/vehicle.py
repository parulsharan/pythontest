
class Vehicle:
    def __init__(self,name,speed_max,mileage) :
        self.name = name
        self.speed_max = speed_max
        self.mileage = mileage

    def show(self):
        print("details: ",self.name,self.speed_max,self.mileage)

    def color(self):
        print("vehicle color is red.")

    def price(self):
        print("vehicle price is $500")