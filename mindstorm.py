import turtle
def draw_square(some_turtle):
    for i in range(1,3):
      some_turtle.forward(100)
      some_turtle.right(120)
      some_turtle.forward(100)
      some_turtle.right(60)

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
    

    window.exitonclick()
draw()

    
