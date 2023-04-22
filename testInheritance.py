from inheritance.bus  import bus
from inheritance.car  import car
from inheritance.truck  import truck



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