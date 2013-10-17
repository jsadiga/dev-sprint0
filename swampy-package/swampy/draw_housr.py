from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

def fdlt(turtle, length=0, angle=90):
	turtle.fd(length)
	turtle.lt(angle)

def fdrt(turtle, length=0, angle=90):
	turtle.fd(length)
	turtle.rt(angle)


def shift(turtle, distance=10):
	turtle.pu()
  	turtle.fd(distance)
  	turtle.pd()

def draw_house(turtle, size=10):
	fdlt(turtle, 3*size)
  	fdrt(turtle, 2*size)
 	fdrt(turtle, 1*size)
  	fdlt(turtle, 2*size)
  	turtle.bk(1*size)
  	fdlt(turtle, 4*size)
  	fdlt(turtle, 4*size, 45)
  	fdlt(turtle, 5*size)
  	fdlt(turtle, 5*size, 45)
  	fdlt(turtle, 4*size)
  	turtle.lt()
  	fdrt(turtle, 4*size)
  	fdrt(turtle, 7*size)
  	fdlt(turtle, 4*size)

draw_house(bob)
#shift(bob)
#draw_house(bob)

wait_for_user()