#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# setting a heading
direction = 0


# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)
  new_color = turtle_colors.pop()
  t.fillcolor()
  t.pencolor()

# set starting configuration
startx = 0
starty = 0

# make turtle move
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.right(45)     
  t.forward(50)
  t.setheading(direction)
  direction = t.heading()
  start_x = t.xcor()
  start_y = t.ycor()

#	change starting coordinates for next turtle shape
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()
