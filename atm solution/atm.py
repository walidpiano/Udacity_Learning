# ATM program
# banknotes: 100, 50, 10, 5, 2, 1

Available = 500


def withdraw(request):
  if request > Available:
    print 'The entered amount is more than the vailable credit!'
  elif request <= 0:
    print 'You have entered invalid amount!'
  else:
    while request != 0:
      if request >= 100:
        request -= 100
        print 'Give 100'
      elif request >= 50:
        request -= 50
        print 'Give 50'
      elif request >= 10:
        request -= 10
        print 'Give 10'
      elif request >= 5:
        request -= 5
        print 'Give 5'
      else:
        print 'Give ' + str(request)
        request = 0
        


withdraw(277)
