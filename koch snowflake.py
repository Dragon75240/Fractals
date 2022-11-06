import turtle

def koch_curve(t, iterations, length, shortening_factor, angle):
     pass
 
t = turtle.Turtle()

t.hideturtle()

for i in range(3):
    koch_curve(t, 3, 200, 0.5, 60)
    t.right(120)
    
turtle.mainloop()