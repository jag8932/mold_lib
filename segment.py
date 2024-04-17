class Segment:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1

    def moveTo(self, newX, newY):
        self.x = newX
        self.y = newY