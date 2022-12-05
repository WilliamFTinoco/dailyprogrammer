class nums:
  def __init__(self, num_a, num_b):
    self.dict = {
      "M":1000,
      "D":500,
      "C":100,
      "L":50,
      "X":10,
      "V":5,
      "I":1
      }
    self.a = 0
    self.b = 0
    for x in num_a:
      self.a += self.dict[x]
    for x in num_b:
      self.b += self.dict[x]
  def numcompare(self):
    if self.a < self.b:
      return("True")
    else:
      return("False")
