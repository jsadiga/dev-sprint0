from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()	

def poly(n,len,angle):
	for i in range(n):
		fd(bob,len)
		lt(bob,angle)

def arc(r,theta):
	n=10
	alen = 2*3.14*r*(theta/360.0)
	len = alen/n
	angle = theta/n
	poly(n,len,angle)

def flowers(num):
	r=60
	theta=60
	for i in range(num):
		arc(r,theta)
		lt(bob,120)
		arc(r,theta)
		rt(bob,200)

flowers(10)
pu(bob)
fd(bob,20)
pd(bob)


wait_for_user()
