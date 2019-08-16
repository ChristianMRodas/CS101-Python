import turtle

my_turtle = turtle.Turtle()

turtle.setup(width=1250, height=650, startx=0, starty=0)


#;rectangle
def rect (x : int,y : int, length : int, width: int, color : str):
    turtle.pu()
    turtle.goto(0,0)
    

    
    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()
    turtle.width(width)

    turtle.pencolor(color)
    
    turtle.fd(length)
 


    #Brush should have rough edges


rect(-100, 75, 200, 50, 'red')
rect(-100, 25, 200, 50, 'green')#FIXME
rect(-100, -25, 200, 50, 'blue')




