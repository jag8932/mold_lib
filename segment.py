class Segment:
    def __init__(self, x1, y1):
        self.x = x1
        self.y = y1
        self.color = "white"
        self.segmentRadius = 5

    def moveTo(self, newX, newY):
        self.x = newX
        self.y = newY

    def change_color(self, col):
        self.color = col
