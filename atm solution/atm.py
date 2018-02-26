# ATM program
# banknotes: 100, 50, 10, 5, 2, 1

Available = 500


def withdraw(reqAmount):
  if reqAmount > Available:
    print 'The entered amount is more than the vailable credit!'
  else:
    while reqAmount != 0:
      if reqAmount >= 100:
        reqAmount -= 100
        print 'Give 100'
      elif reqAmount >= 50:
        reqAmount -= 50
        print 'Give 50'
      elif reqAmount >= 10:
        reqAmount -= 10
        print 'Give 10'
      elif reqAmount >= 5:
        reqAmount -= 5
        print 'Give 5'
      else:
        print 'Give ' + str(reqAmount)
        reqAmount = 0
        


withdraw(277)
