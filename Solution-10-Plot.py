#Solution for problem 10
#import matplotlib.pyplot as plt
#plt.plot([1,2,3,4])
#plt.ylabel('some numbers')
#plt.show()

import numpy as np
import matplotlib.pyplot as pl

data =np.genfromtxt('Faith.csv',delimiter=',',skip_header=True)
firstcol = data[:,0]
meanfirstcol = numpy.mean(data[:,0])


print("Average " ,meanfirstcol)

#pl.hist(firstcol)
#numpy.min(firstcol)
#numpy.max(firstcol)