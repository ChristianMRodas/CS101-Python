import turtle

turtle.screensize(1500,2000)

my_turtle = turtle.Turtle()




#;rectangle
def star (x : int,y : int, angle : int, length: int, color : str):
    turtle.pu()
    turtle.goto(0,0)
    
    turtle.setx(x)
    turtle.sety(y)
    turtle.pd()
    turtle.width(3)

    turtle.pencolor(color)
    turtle.seth(angle)
    turtle.fd(length)
 


    


star(-200, 200, 0, 400, 'blue')
star(200, 200, -144, 400, 'red')
star(-124, -35, 72, 400, 'green')
star(0, 345, 288, 400, 'black')
star(124, -35, 144, 400, 'purple')




