This program simulates the basic logic required for the Molds' behaviors. Using Python's Tkinter canvas api and vector math, 
the bloby mold type chases after nearby attractor molds. Attractor molds are in constant free float mode and move around the 
canvas aimlessly. 

The blobby mold is comprised of segments. Each segment is a point on the canvas and the program checks for the furthest segment to
a nearby attractor mold. The furthest segment is placed next to the closest segment to the attractor. By having the mold 'move' this way
we were intending for the mold to look like it was reaching out to the food source with TouchDesigner effects on top of it. 

In Tkinter's canvas, the molds are represented by ellipses. 
