import random
import math

class Attractor:
  
  centerPoint = [250, 250]

  def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
        self.speedX = random.randint(1, 3)
        self.speedY = random.randint(1, 3)

  def floatMode(self):
        self.x += self.speedX
        self.y += self.speedY
        if self.find_distance(self.x, self.y, self.centerPoint[0], self.centerPoint[1]) > 250:
          self.speedX *= -1
          self.speedY *= -1

  def find_distance(self, x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance 