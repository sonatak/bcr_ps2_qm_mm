# These are the external libraries which import the functions to
# Read data
from pandas import read_csv
# Do the fitting
from symfit import parameters, variables, sin, cos, Fit
# Transform into standarized compatible numeric data type
import numpy as np
# Represent the data
import matplotlib.pyplot as plt
import math

# Define constants and files to read
### !!!!!!! Line to change
fname="angle2"
### !!!!!!! Line to change
fit_output = open(fname + ".fit", "w+")
file1 = "qm" + fname +".dat"
print(file1)
file2 = fname + ".dat"
qmdata = read_csv(file1,sep="    ",header=None) #this input must be in same folder
ff0data = read_csv(file2,sep="    ",header=None) #this input must be in same folder
kdist1=482996.338
kdist2=254544.042
kdist3=425754.575
kang1=533.4864
kang2=635.6797

# It stores X in first column, [0], and Y in sixth, [5]
xdata = np.array(qmdata[0])
#print(xdata)

ydata = -( np.radians(np.array(qmdata[1]-ff0data[1])) * kang2 )
# Instance x and y
x, y = variables('x, y')

def fourier_series():
    """
    Returns the desired fourier series.
    """
    # Define fourier variables and sine
    a0,a1,a2,a3,a4,a5,a6 = parameters(','.join(['a{}'.format(i) for i in range(0, 7)]))
    return a0*(1+sin(-1.571)) \
      + a1*(1+sin(1*x+1.571)) \
      + a2*(1+sin(2*x-1.571)) \
      + a3*(1+sin(3*x+1.571)) \
      + a4*(1+sin(4*x-1.571)) \
      + a5*(1+sin(5*x+1.571)) \
      + a6*(1+sin(6*x-1.571))

# Variable which stores the fitting formula
model_dict = {y: fourier_series()}
# outputs {y: a0*(sin(x + 1.571) + 1) + a1*(sin(2*x - 1.571) + 1) + a2*(sin(3*x + 1.571) + 1) \
#   + a3*(sin(4*x - 1.571) + 1) + a4*(sin(5*x + 1.571) + 1) + a5*(sin(6*x - 1.571) + 1)}

# Define a Fit object for this model and data
fit = Fit(model_dict, x=np.radians(xdata), y=ydata)
fit_result = fit.execute()
#print(parameters)
fit_output.write(str((fit_result)))
#print(fit_result)

# These are the fitting values to align with X array data
fit_aligned = fit.model(x=xdata, **fit_result.params).y

# Plot the result
plt.ylabel('Fit data')
plt.xlabel('Dihedral, radians')
plt.grid(True)
plt.title(fname)
plt.plot(np.radians(xdata),ydata)
plt.plot(np.radians(xdata), fit.model(x=np.radians(xdata), **fit_result.params).y, color='red', ls=':')
np.savetxt(fname+ '.out', (np.c_[xdata, ydata, fit_aligned]), fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)
plt.savefig(fname+'.eps')
# In this point, it is shown the plot; the fitting is colored in red, the data is colored in blue
