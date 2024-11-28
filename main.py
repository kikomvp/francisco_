import turtle
import time
import random


delay = 0.1
score = 0
high_score=0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)


head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("green")
head.penup()
head.goto(0,0)
head.direction = "Stop"


food = turtle.Turtle()
colors = random.choice(['red','blue','yellow'])
shapes = random.choice(['square','circle','triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0,100)


segments = []
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,250)
pen.write("Score : 0 High Score: 0", align = "center", font = ("arial",24,"bold"))

def goup():
    if head.direction != "down":
        head.direction = "up"
def godown():
    if head.direction != "up":
        head.direction = "down"
def goleft():
    if head.direction != "right":
        head.direction = "left"
def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

while True:
    wn.update()
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.3)
        head.goto(0,0)
        head.direction = "Stop"
        colors = random.choice(['red','blue','green'])
        shapes = random.choice(['square','circle'])
        score=0
        pen.clear()
        pen.write(f"Score : {score} High Score: {high_score}", align = "center", font = ("arial",24,"bold"))

    if head.distance(food)<20:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))
        score+=1
    time.sleep(delay)
wn.mainloop()







































































