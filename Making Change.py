def makingChange(units):
  if units == 0:
    return(0)
  else:
    coins = 0
    while units > 0:
      if units >= 500:
        units += -500
        coins += 1
      else if units >= 100:
        units += -100
        coins += 1
      else if units >= 25:
        units += -25
        coins += 1
      
