import turtle 

t= turtle.Turtle()
turtle.bgcolor("black") 
t.speed(500)
for i in range(180):
    step=300

    if i%2==0:
        t.color("magenta")
        step=300
    elif i%3==0:
        t.color("cyan")
        step=250
    elif i%5==0:
        t.color("yellow")
        step=150
    else:
        t.color("white")
        step=100

    t.forward(step)
    t.dot(6)
    t.backward(step)   
    t.right(2)


#RB
t= turtle.Turtle()
def semi_circle(col, rad, val):
    t.color(col)
    t.circle(rad, -180)
    t.up()
    t.setpos(val, 0)
    t.down()
    t.right(180)
colores=['magenta', 'indigo', 'cyan','green', 'yellow', 'orange', 'red']
t.right(90)
t.width(10)
t.speed(7)

for i in range(7):
    semi_circle(colores[i], 10*(i + 8), -10*(i + 1))


#J
t=turtle.Turtle()
t.speed(3)
t.shape("circle")
t.color("pink")
t.pensize(35)
t.penup()
t.goto(-300,50)
t.pendown()
t.fd(10)
t.rt(90)
t.fd(150)
t.circle(-50,180)

#A
t.color("pink")
t.penup()
t.goto(-250,-130)
t.pendown()
t.rt(25)
t.fd(150)
t.rt(130)
t.fd(150)
t.penup()
t.lt(160)
t.fd(40)
t.lt(85)
t.fd(15)
t.pendown()
t.fd(90)

#V
t=turtle.Turtle()
t.speed(3)
t.shape("circle")
t.color("pink")
t.pensize(35)
t.penup()
t.goto(-120,10)
t.pendown()
t.rt(65)
t.fd(150)
t.rt(-130)
t.fd(150)

#I
t=turtle.Turtle()
t.speed(3)
t.color("pink")
t.pensize(35)
t.penup()
t.goto(60,10)
t.pendown()
t.rt(90)
t.fd(140)

#E
t=turtle.Turtle()
t.speed(3)
t.color("pink")
t.pensize(35)
t.penup()
t.goto(230,10)
t.pendown()
t.lt(180)
t.fd(110)
t.lt(90)
t.fd(70)
t.lt(90)
t.fd(90)
t.lt(180)
t.fd(90)
t.lt(90)
t.fd(70)
t.lt(90)
t.fd(110)


#R
t=turtle.Turtle()
t.speed(3)
t.color("pink")
t.pensize(35)
t.penup()
t.goto(280,10)
t.pendown()
t.fd(120)
t.rt(90)
t.fd(80)
t.rt(90)
t.fd(120)
t.rt(90)
t.fd(80)
t.rt(180)
t.fd(140)
t.rt(180)
t.fd(80)
t.rt(120)
t.fd(160)
t.lt(40)


turtle.done()