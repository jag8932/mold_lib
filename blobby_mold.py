import math;
from segment import Segment

class BlobbyMold:
    # Health status will simply be an integer and deteriorate over
    # timer if the mold doesn't find food. 
    health_status = 5 
    radius = 10
    closestFoodPos = [0, 0]
    closestSegmentPos = [0, 0]
    def __init__(self, position, segments):
        self.position = position
        self.totalSegments = segments
        self.segmentPos = []
        for i in range(self.totalSegments):
            i = Segment(self.position[0] + i * self.radius, self.position[1] + i * self.radius)
            self.segmentPos.append(i)

    def find_distance(self, x1, y1, x2, y2):
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance
    
    def closest_food(self, list):
        shortestDistance = self.find_distance(self.position[0], self.position[1], list[0].x, list[0].y)
        nearestFood = list[0]
        for i in list:
            refDist = self.find_distance(self.position[0], self.position[1], i.x, i.y)
            if refDist < shortestDistance:
                shortestDistance = refDist
                nearestFood = i 

        self.closestFoodPos = [nearestFood.x, nearestFood.y]        
        return shortestDistance
                
            

# segmentX and Y refer to a segment's given position. Targets is an array of all food positions on the map


obj = BlobbyMold([1, 0], 5)

print(obj.position)

for segPos in obj.segmentPos:
    print(segPos.x, segPos.y)

