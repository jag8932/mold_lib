import random

class Attractor:
    
  def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
        self.speedX = random.randint(1, 3)
        self.speedY = random.randint(1, 3)

  def floatMode(self):
        self.x += self.speedX
        self.y += self.speedY
        if self.x > 499 or self.x < 1:
          self.speedX *= -1
        if self.y > 499 or self.y < 1:
          self.speedY *= -1
