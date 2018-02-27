class ATM:
  
  def __init__(self, balance, bank_name):
    self.balance = balance
    self.bank_name = bank_name
  
  def withdraw(self, request):
    print 'Wecome to ' + self.bank_name
    print 'current balance = ' + str(self.balance)
    print '=================================='
    if request > self.balance:
      print("Can't give you all this money !!")
  
    elif request <= 0:
      print("More than zero plz!")
  
    else:
      self.balance -= request
      while request > 0:
  
        if request >= 100:
          request -= 100
          print("give 100")
  
        elif request >= 50:
          request -= 50
          print("give 50")
  
        elif request >= 10:
          request -= 10
          print("give 10")
  
        elif request >= 5:
          request -= 5
          print("give 5")
  
        elif request < 5:
          print("give " + str(request))
          request = 0
    print '=================================='  
    return self.balance



balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)
