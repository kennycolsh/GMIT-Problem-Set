#Solution for problem 10
#https://pythonspot.com/matplotlib-legend/
 

import numpy as np
import matplotlib.pyplot as pl

#data =np.genfromtxt('Faith.csv',delimiter=',',skip_header=True)
#firstcol = data[:,0]
#meanfirstcol = np.mean(data[:,0])
#pl.hist(firstcol)
#pl.show()
#print("Average " ,meanfirstcol)

#pl.hist(firstcol)
#numpy.min(firstcol)
#numpy.max(firstcol)

#set up the array
#start, stop, step
x = np.arange(0, 4, .5)
#create the variables
y_1 = x
y_2 = x**2
y_3 = 2**x
#plot the graph and create the label
pl.plot(x, y_1, label='y=x')
pl.plot(x, y_2, label='y=x^2')
pl.plot(x, y_3, label='y=2^x')
#give it grid lines
pl.grid()
#add legends to make it more readable
pl.legend()
#give the graph a title
pl.title('Solution 10')
#show the Plot
pl.show()
