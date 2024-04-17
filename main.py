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
    for f in list:
        if obj.find_distance(obj.position[0], obj.position[1], f.x, f.y) == closest:
            circle(canvas, f.x, f.y, 10, "blue")
        else:
            circle(canvas, f.x, f.y, 10, "black")

def draw_blobby(canvas, obj):
    for segment in obj.segmentPos:
        circle(canvas, segment.x, segment.y, obj.radius, "red")

def update_canvas():
    global posX, posY, food, blobby
    C.delete("all")
    C.create_rectangle(0, 0, 250, 300, fill="yellow")
    
    draw_blobby(C, blobby)
    draw_food(C, food, blobby)
    C.after(100, update_canvas)
    



spawn_food()
update_canvas()
mainloop()
