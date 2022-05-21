from turtle import *
#forward(200)
#left(90)
#backward(200)
#right(90)
#circle(200)
def heart(x,y,size):
    goto(x,y)
    left(150)
    begin_fill()
    forward(51*size)
    ring(150,size,0.3,'right')
    ring(210,size,0.786,'right')
    left(120)
    ring(210,size,0.786,'right')
    ring(150,size,0.3,'right')
    forward(51*size)
    end_fill()

heart(200,200,5)

