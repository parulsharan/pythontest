class vehicle:
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


# first child class/////
class car(vehicle):
    def color(self):
        print("car color is green.")

    def price(self):
        print("car price is $400.") 


# second child class//////
class bus(vehicle):
    pass   


# third child class/////
class truck(vehicle):
    def color(self):
        print("truck color is black.")


# object with child class bus///////
school_bus = bus("abc", 120,12)
school_bus.color()
school_bus.price()
print("vehicle name: ",school_bus.name,"speed: ",school_bus.speed_max,"mileage: ",school_bus.mileage)


# object with child class car///
car1 = car("jetta", 110,22)
car1.color()
car1.price()
print("vehicle name: ",car1.name,"speed: ",car1.speed_max,"mileage: ",car1.mileage,)

# object with third class/////
trk = truck("gmc",150,32)
trk.color()
print("vehicle name: ",trk.name,"speed: ",trk.speed_max,"mileag: ",trk.mileage)