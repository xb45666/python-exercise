import numpy as np


position=[]
velocity=[]
a=72
b=-1512
c=26712
m=1
h=0.002
pos=1.0001
ppos=pos
n=20
i=1

for i in range(n):
	ac = (a*pos+0.5*b*pos**2+1/6*c*pos**3)/m#acceleration
	newpos=2*pos-ppos+ac*h**2#new position
	v=(newpos-ppos)/(2*h)#velocity at pos

	position.append(newpos)
	velocity.append(v)

	ppos=pos
	pos=newpos
print(position)
#f = open("x.txt",'wb')
#f.write(position)
#f.close()
#f = open("v.txt",'wb')
#f.write(velocity)
#f.close()
#np.save('x.py',position)
#np.save('v.py',velocity)