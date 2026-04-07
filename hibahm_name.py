from turtle import *
screen = Screen()
screen.title("HIBAH in Color")
screen.bgcolor("black")
screen.setup(width=1000, height=500)

############# LETTER: H ###################################
t1 = Turtle()
t1.pensize(12)
t1.color("red")
t1.speed(3)
t1.penup()
t1.goto(-400, -100)
t1.pendown()

t1.setheading(90)
t1.forward(200)
t1.backward(100)
t1.setheading(0)
t1.forward(80)
t1.setheading(90)
t1.forward(100)
t1.backward(200)

############# LETTER: I ###################################
t2 = Turtle()
t2.pensize(12)
t2.color("orange")
t2.speed(3)
t2.penup()
t2.goto(-250, 100)
t2.pendown()

t2.goto(-170, 100)
t2.penup()
t2.goto(-210, 100)
t2.pendown()
t2.goto(-210, -100)
t2.goto(-250, -100)
t2.goto(-170, -100)

############# LETTER: B ###################################
t3 = Turtle()
t3.pensize(12)
t3.color("yellow")
t3.speed(3)
t3.penup()
t3.goto(-100, -100)
t3.pendown()

t3.goto(-100, 100)
t3.setheading(0)
t3.circle(-50, 180)
t3.setheading(0)
t3.circle(-50, 180)

############# LETTER: A ###################################
t4 = Turtle()
t4.pensize(12)
t4.color("green")
t4.speed(3)
t4.penup()
t4.goto(10, -100)
t4.pendown()

t4.goto(50, 100)
t4.goto(100, -100)
t4.penup()
t4.goto(85, 0)
t4.pendown()
t4.goto(15, 0)

############# LETTER: H ###################################
t5 = Turtle()
t5.pensize(12)
t5.color("blue")
t5.speed(3)
t5.penup()
t5.goto(200, -100)
t5.pendown()

t5.goto(200, 100)
t5.goto(200,50)
t5.goto(200, 0)
t5.goto(280, 0)
t5.goto(280, 100)
t5.goto(280, -100)



screen.exitonclick()