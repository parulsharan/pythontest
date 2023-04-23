class Seats:
    def __init__(self,capcity,is_front_warm):
        self.capcity = capcity
        self.is_front_warm = is_front_warm

    def seat_describe(self):
        print(str(self.capcity) + " seats and are those warm: " + str(self.is_front_warm))    