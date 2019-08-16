import turtle

my_turtle = turtle.Turtle()

x = 25
l = 100

my_turtle = turtle.home()



def draw_circle (x : int,y : int,radius : int, color : str):
    turtle.pu()
    

    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.circle(radius)
    turtle.end_fill()
    turtle.ht()





my_turtle = draw_circle(-50,50,100, 'blue',)
my_turtle = draw_circle(50,-50,100,'green')
my_turtle = draw_circle(0,0,100,'red')
