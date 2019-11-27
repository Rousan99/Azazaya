import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
	return 4.0*x

def Euler1(f,x_start,y_start,h,x_max):
	x_array, y_array, dydx_array = [], [], []
	while abs(x_start)<abs(x_max):
		dydx = f(x_start,y_start)
		x_array.append(x_start);y_array.append(y_start);dydx_array.append(dydx)
		y_start = y_start + h*dydx
		x_start = x_start + h
	return x_array, y_array

it = ['blue','green','yellow']

x_start , y_start, h, x_max = 0.0, 0.0, 0.01, 10.0
xx = np.arange(0.0,10.0,0.5)
i = 0
h = 0.01
while h<1.05:
	x_start = 0
	y_start = 0
	Xarr , Yarr = Euler1(f,x_start,y_start,h,x_max)
	#print(Xarr)
	#print(Yarr)
	tt = "h=%.4f"%(h)
	plt.plot(Xarr,Yarr,it[i],label=tt)
	h += 0.5
	i += 1
plt.plot(xx,2*xx**2,'red',label="Exact Solution")
plt.legend(loc='best',prop={'size':12})
plt.xlabel("x");plt.ylabel("y")
plt.title("Comparison between true and Euler solution:")
plt.show()
