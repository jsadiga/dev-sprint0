# Polygon excercise from Week 0

# Name:shishira adiga


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob
'''def polygon(len,n):
	for i in range(n):
		fd(bob,len)
		rt(bob,360/n)

#polygon(25,5)

def circle(r):
	n=10
	len = (2*3.14*r)/n
	polygon(len,n)

def arc(r,theta):
	n=10
	len1 =2*3.14*r*(theta/360)
	len = len



circle(8)'''

def poly(n,len,angle):
	for i in range(n):
		fd(bob,len)
		lt(bob,angle)

def polygon(n,len):
	angle = 360.0/n
	poly(n,len,angle)

def arc(r,theta):
	n=10
	alen = 2*3.14*r*(theta/360.0)
	len = alen/n
	angle = theta/n
	poly(n,len,angle)

def circle(r):
	arc(r,360)

arc(50,90)

wait_for_user()					
