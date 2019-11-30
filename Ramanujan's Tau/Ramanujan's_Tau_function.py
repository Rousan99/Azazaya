def sigma(n):
	sum=0
	for i in range (1,n+1):
		if n%i==0:
			sum=sum+i
		else:
			pass
	return sum
def tau(p):
	return (p**4)*sigma(p) - 24*sum( ( (35*k**4 - 52*p*k**3 + 18*(p**2)*(k**2) )*sigma(k)*sigma(p-k) ) for k in range(1,p))

for i in range(1,301):
	if i%3==0:
	    print("tau(",i,") = ",tau(i))
