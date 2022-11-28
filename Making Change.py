def makingChange(units):
  if units == 0:
    return(0)
  else:
    coins = 0
    coinlist = [500, 100, 25, 10, 5, 1]
    currentcoin = 0
    while units > 0:
      if units >= coinlist[currentcoin]:
        units -= coinslist[currentcoin]
        coins += 1
      else:
        currentcoin += 1
    return(coins)
