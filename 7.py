position=[]
velocity=[]
a=72
b=-1512
c=26712
m=1
h=0.02
pos=0
ppos=0
n=20

while i <= n :
	ac = (a*pos+0.5*b*x**2+1/6*c*x**3)/m#acceleration
	newpos=2*pos-ppos+ac*h**2#new position
	velocity=(newpos-ppos)/(2*h)#velocity at pos

	position=position.append(newpos)
	velocity=velocity.append(velocity)

	ppos=pos
	pos=newpos
	i=i+1
print(position)