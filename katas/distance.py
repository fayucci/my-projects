import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def distance(self, b):
      return math.sqrt((b.x - self.x)**2 + (b.y - self.y)**2)

a = Point(1,1)

b = Point(2,2) 

print(a.distance(b))
