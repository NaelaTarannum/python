import turtle

def draw_triangle(some_turtle,length,ori,recursion):
    recursion=recursion+1
    #naela=some_turtle

    for i in range(0,3):
        if(recursion<4):
            naela.forward(length/2)
            naela.left(120)
            draw_triangle(naela,length/2,0,recursion)
            naela.right(120)
            naela.forward(length/2)
        else:
          naela.forward(length)
        if (ori==1):
            naela.left(120)
        else:
            naela.right(120)

naela = turtle.Turtle() 
naela.speed(10) 
naela.color("green") 
naela.shape("turtle") 
window = turtle.Screen()  
window.bgcolor("red")     # set background color to red


draw_triangle(naela,200,1,0)



window.exitonclick()      
