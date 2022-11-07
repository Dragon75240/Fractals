from turtle import Turtle

def draw_sierpinski(length,depth):
    if depth==0:
        for i in range(0,3):
            Turtle.fd(length)
            Turtle.left(120)
    else:
        draw_sierpinski(length/2,depth-1)
        Turtle.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        Turtle.bk(length/2)
        Turtle.left(60)
        Turtle.fd(length/2)
        Turtle.right(60)
        draw_sierpinski(length/2,depth-1)
        Turtle.left(60)
        Turtle.bk(length/2)
        Turtle.right(60)