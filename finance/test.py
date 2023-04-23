from person import Person
from account import Account

parul = Person("Parul Mann", "seasons", "9259977352")
print("parul: ", parul.name,parul.address, parul.phone)

# kamal = Person("Kamal Mann ", "seasons", "9259156341")
# print("kamal: ",kamal.describe())

parul_acc = Account(parul, 989898)
# print("account details: ", parul_acc.person.describe(), parul_acc.total_money)
print(parul_acc.passbook())


parul_acc.deposit(-1000000000)
print(parul_acc.passbook())

parul_acc.withdrawl(1000000)
print(parul_acc.passbook())