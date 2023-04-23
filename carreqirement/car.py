from seats import Seats

class Car:
    def __init__(self,engine,fuel_tank,seats: Seats,license):
        self.engine = engine
        self.fuel_tank = fuel_tank
        self.seats = seats
        self.license = license
        

    def describe(self):
        print(self.engine, self.fuel_tank, self.seats.seat_describe(), self.license)

        