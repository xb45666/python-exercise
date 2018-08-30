def maxsum(a,b,c=2):
	""" return the biggest sum between any 2 numbers among a,b,c.

	>>> maxsum(1,2,3)
	5 
	"""
	sum1=a+b
	sum2=b+c
	sum3=a+c
	return max(sum1,sum2,sum3)

print(maxsum(1,2,3),1,2,3,sep='\n')



negativesum = lambda a,b : -(a+b)


print(negativesum(2,3))