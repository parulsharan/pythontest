from car import Car

class Pilot(Car):
    def __init__(self, engine, fuel_tank, seats, license):
        super().__init__(engine, fuel_tank, seats, license)

    def describe(self):
        print("pilot: ", self.engine,self.fuel_tank, self.seats, self.license)




            