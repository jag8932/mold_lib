import tkinter
import random
from tkinter import *
from blobby_mold import BlobbyMold
from attractor import Attractor


blobby = BlobbyMold([10, 20], 5)
root = Tk()
 
C = Canvas(root, bg="yellow",
           height=500, width=500)

C.pack()

posX = 10
posY = 10
food = []

def spawn_food():
    for i in range(10):
        i = Attractor(random.randint(1, 499),random.randint(1, 499))
        food.append(i)

def circle(canvas,x, y, radius, color):
    ellipse = canvas.create_oval(x, y, x + radius, y + radius, fill=color)

def draw_food(canvas, list, obj):
    closest = obj.closest_food(list)
    global linex, liney
    for f in list:
        if obj.find_distance(obj.position[0], obj.position[1], f.x, f.y) == closest:
            circle(canvas, f.x, f.y, 10, "blue")
            linex = f.x
            liney = f.y
            vector = obj.unit_vector(obj.position[0], obj.position[1], linex, liney)
            canvas.create_line(obj.position[0], obj.position[1], obj.position[0] + vector[0] * 50, obj.position[1]+ vector[1] * 50)
        else:
            circle(canvas, f.x, f.y, 10, "black")
        
def consume_food(obj, list):
    for i in list:
        if obj.find_distance(obj.generalPosition[0], obj.generalPosition[1], i.x, i.y) < obj.radius*2:
            list.remove(i)
            return
    
def draw_blobby(canvas, obj):
    for segment in obj.segmentPos:
        circle(canvas, segment.x, segment.y, obj.radius, segment.color)

def update_food(list):
    for i in list:
        i.floatMode()

def update_canvas():
    global posX, posY, food, blobby
    C.delete("all")
    C.create_rectangle(0, 0, 500, 500, fill="white")
    
    draw_blobby(C, blobby)
    draw_food(C, food, blobby)
    update_food(food)
    blobby.update_segments()
    consume_food(blobby, food)

    if len(food) < 1:
        spawn_food()
    C.after(50, update_canvas)
    



spawn_food()
update_canvas()
mainloop()

