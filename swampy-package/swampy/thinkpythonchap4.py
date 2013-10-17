# thinkpython chap4

from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob

#wait_for_user()

'''def square(t,l):
	for i in range(4):
		fd(t,l)
		rt(t)

square(bob,40)'''

def polygon(t,l,n):
	for i in range(n):
		fd(t,l)
		rt(t,360/n)

#polygon(bob,20,5)

def circle(t,r):
	n=2
	l=(2*3.14*r)/n
	
	polygon(t,l,n)

#circle(bob,10)


def arc(t,r,angle):
	n=20
	l=(2*3.14*r)/n
	
	polygon(t,l,n)

wait_for_user()
