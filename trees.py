import turtle
import random

t = turtle.Turtle()

t.speed(0)
t.color("Green")
t.pensize(3)

treesXs = []
treesYs = []
def createMathForest(sz):
    for i in range(sz):
        treesXs.append(random.randint(-100,100))
        treesYs.append(random.randint(-100,100))    
def createTree(sz,x,y,color):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(sz)
    t.end_fill()
def createForest(aot):
    createMathForest(aot+1)
    for i in range(len(treesXs)-1):       
        createTree(10,treesXs[i+1],treesYs[i+1],"Green")

createForest(int(input("How many trees would you like: ")))

t.hideturtle()
turtle.exitonclick()


