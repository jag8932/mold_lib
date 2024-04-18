import math;
import random
from segment import Segment

class BlobbyMold:
    # Health status will simply be an integer and deteriorate over
    # timer if the mold doesn't find food. 
    health_status = 5 
    radius = 10
    closestFoodPos = [0, 0]
    closestSegmentPos = [0, 0]
    generalPosition = [0, 0]
    def __init__(self, position, segments):
        self.position = position
        self.totalSegments = segments
        self.segmentPos = []
        for i in range(self.totalSegments):
            i = Segment(self.position[0] + random.randint(1,3), self.position[1] + random.randint(1,3))
            self.segmentPos.append(i)

    def find_distance(self, x1, y1, x2, y2):
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance
    
    def closest_food(self, list):
        shortestDistance = self.find_distance(self.generalPosition[0], self.generalPosition[1], list[0].x, list[0].y)
        nearestFood = list[0]
        for i in list:
            refDist = self.find_distance(self.generalPosition[0], self.generalPosition[1], i.x, i.y)
            if refDist < shortestDistance:
                shortestDistance = refDist
                nearestFood = i 

        self.closestFoodPos = [nearestFood.x, nearestFood.y]        
        return shortestDistance

    def furthest_segment(self): 
        furthest = self.segmentPos[0]
        for i in self.segmentPos:
            if self.find_distance(i.x, i.y, self.closestFoodPos[0], self.closestFoodPos[1]) > self.find_distance(furthest.x, furthest.y, self.closestFoodPos[0], self.closestFoodPos[1]):
                furthest = i 
        furthest.change_color("red")
        return furthest

    def closest_segment(self): 
        closest = self.segmentPos[0]
        for i in self.segmentPos:
            if self.find_distance(i.x, i.y, self.closestFoodPos[0], self.closestFoodPos[1]) < self.find_distance(closest.x, closest.y, self.closestFoodPos[0], self.closestFoodPos[1]):
                closest = i 
        closest.change_color("green")
        return closest

    def unit_vector(self, x1, y1, x2, y2):
        legX = x2 - x1
        legY = y2 - y1
        theta = math.atan2(legY, legX)        
        return [math.cos(theta), math.sin(theta)]         
    
    def update_segments(self):
        furthestSeg = self.furthest_segment()
        closestSeg = self.closest_segment()
        direction = self.unit_vector(closestSeg.x, closestSeg.y, self.closestFoodPos[0], self.closestFoodPos[1])
        furthestSeg.moveTo(closestSeg.x + direction[0]*self.radius, closestSeg.y + direction[1]*self.radius)
        self.generalPosition = [furthestSeg.x, furthestSeg.y]