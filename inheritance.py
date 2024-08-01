class Action:
  def __init__(self, name):
    self.name = name

  def func_wash(abc):
    print(abc.name + " is washed.")

class Cooking(Action):
  def __init__(self, name):
    self.name = name

  def func_cut(abc):
    print(abc.name + " is cut.")

  def func_masala(abc):
    print(abc.name + " is mixed with masala.")

  def func_oven(abc):
    print(abc.name + " is in the oven.")

p1 = Cooking("Meat")
p2 = Cooking("Fish")
p3 = Cooking("Vegetable")

p1.func_wash()
p1.func_cut()
p1.func_masala()
p1.func_oven()

p2.func_wash()
p2.func_cut()
p2.func_masala()
p2.func_oven()

p3.func_wash()
p3.func_cut()
p3.func_masala()
p3.func_oven()