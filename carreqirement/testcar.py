# from car import Car
from jetta import Jetta
from pilot import Pilot
from seats import Seats
jetta_seats = Seats(5,False)
car1 = Jetta("v4", 20, jetta_seats,"ed123")
car1.describe()