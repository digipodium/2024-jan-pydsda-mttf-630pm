from turtle import *
speed(0)

def polygon(side,size,color):
    pencolor(color)
    for _ in range(side):
        fd(size)
        lt(360/side)

# testing the function
for i in range(6):
    polygon(side = 10, size=50, color='red')
    polygon(side = 6, size=100, color='blue')
    polygon(4, 100, color='green')
    lt(60)

hideturtle()
mainloop()