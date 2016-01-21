#import numpy and matlibplots module
import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, cos, pi

#generate array of x values from 0 to 6pi
x = np.linspace(0, 6*pi)
line, = plt.plot(x, np.sin(x), linewidth=1)

#calculate y values for sin wave
ysin=sin(x)

#calculate y values for cosine wave
ycos=cos(x)
    
#plot x and y values for both functions
plt.plot(x,ycos)    

plt.ylabel("y")
plt.xlabel("x")

#add legend
plt.legend(("sin(x)", "cos(x)"))

#set dashed line for sine wave and solide line for cosine wave        
dashes = [10, 5, 100, 5]  
line.set_dashes(dashes) 
plt.show()

#Name: Ikenna Onyenze
#ID: 02754297
#Date: 1/19/2016