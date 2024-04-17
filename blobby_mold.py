import math;

class BlobbyMold:
    # Health status will simply be an integer and deteriorate over
    # timer if the mold doesn't find food. 
    health_status = 5 
    radius = 1

    def __init__(self, position, segments):
        self.position = position
        self.segments = segments
        self.segmentPos = []
        for i in range(self.segments):
            i = [self.position[0] + 1 * i, self.position[1]  + 1 * i]
            self.segmentPos.append(i)

    def find_distance(self, x1, y1, x2, y2):
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance

    
obj = BlobbyMold([1, 0], 5)

print(obj.segments)
print(obj.segmentPos)
print(obj.find_distance(3, 5, 4, 10))