from turtle import *
pensize(2)
#black circle
color("black")
begin_fill()
circle(60)
end_fill()
penup()

#red circle
color("red")
goto(100,100)
pendown()
begin_fill()
circle(20)
end_fill()
penup()

#blue circle
color("blue")
goto(-100,100)
pendown()
begin_fill()
circle(40)
end_fill()
penup()
#green circle 
color("green")
goto(-100,-100)
pendown()
begin_fill()
circle(30)
end_fill()
penup()
#yellow circle
color("yellow")
goto(100,-100)
pendown()
begin_fill()
circle(80)
end_fill()
penup()

hideturtle()
exitonclick()