import turtle
from Modules.serpinskiTriangle import draw_sierpinski
from Modules.kochSnowflake import koch_curve

print("Press 1 for Sierpinski Triangle, Press 2 for Koch Snowflake, Press 3 for the Basic Tree")
FracCheck = input("Enter 1, 2, 3: ")
intFracCheck = int(FracCheck)

if intFracCheck not in [1,2,3]:
    print("Invalid input")
    exit()
elif intFracCheck == 1:
    lengthCheck = input("Enter the length of the triangles: ")
    depthCheck = input("Enter the depth of the triangles: ")
    
    draw_sierpinski(int(lengthCheck), int(depthCheck))
elif intFracCheck == 2:
    iterationsCheck = input("Enter the number of iterations: ")
    lengthCheck = input("Enter the length of the triangles: ")
    shortening_factorCheck = input("Enter the shortening factor: ")
    angleCheck = input("Enter the angle: ")
    
    for i in range(3):
        koch_curve(turtle.Turtle(), int(iterationsCheck), int(lengthCheck), int(shortening_factorCheck), int(angleCheck))
        turtle.Turtle().right(120)