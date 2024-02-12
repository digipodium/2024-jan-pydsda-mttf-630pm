from turtle import *

speed('fastest')

s = 0
while s < 500:
    fd(50 + s)
    lt(60)
    write(s)
    dot(10)
    s += 5
hideturtle()
mainloop()