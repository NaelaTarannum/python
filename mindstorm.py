import turtle
def draw_square(some_turtle):
    for i in range(1,3):
      some_turtle.forward(100)
      some_turtle.right(120)
      some_turtle.forward(100)
      some_turtle.right(60)
#def draw_circle(some_turtle):
    #some_turtle.circle(100)
#def draw_tri(tom):
#    tom.forward(100) 
#    tom.left(120)
#    tom.forward(100)
#    tom.left(120)
#    tom.forward(100)
def draw():
    naela=turtle.Turtle()
    window=turtle.Screen()
    window.bgcolor("red")
   
    naela.color("pink")
    naela.speed(10)
    for i in range(1,37):
      draw_square(naela)
      naela.right(10)
    naela.right(90)
    naela.forward(200)
    #rhys=turtle.Turtle()
    #naela.goto(50)
    #rhys.penup()
    #rhys.backward(50)
    #rhys.pendown()
    #rhys.shape("turtle")
    #rhys.color("black")
    #draw_circle(rhys)
    #rhys.penup()
    #rhys.backward(200)
    #rhys.pendown()
    #draw_tri(rhys)

    window.exitonclick()
draw()

    
