from person import Person

class Account:
    def __init__(self, person, total_money):
        self.person = person
        self.total_money = total_money
        
    def deposit(self, input_money):
        if input_money < 1:
            print("invalid money inform 911")
        else:    
            self.total_money += input_money
            print("total money: ",self.total_money)

    def withdrawl(self, money):
        if money > self.total_money :
            print("insufficient money")
        else:    
            self.total_money -= money       
            print("total money: ",self.total_money)

    def passbook(self):
        return "account details: " + self.person.describe() + "\n" + "$ " + str(self.total_money)