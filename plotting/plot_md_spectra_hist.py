import os 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot
import scipy.stats as sts
from mpl_toolkits import mplot3d




#### Reading data

snapshots = os.listdir('./data/')

token=[]
token2=[]
energy=[]
fosc=[]

for snapshot in snapshots:
    f=open(str("./data/"+snapshot),"r")
    line=f.readlines()
    k=0
    for item in line:
        k=+1
        if "Excited State   1" in item:
            columns=" ".join(item.split())
            token.append(
                #str(snapshot+" "+str(k)+" "+
                columns.split(" ")[4]
                #)
            )
            token2.append(columns.split(" ")[8])

for item in token:
    energy.append(float(item))

for item in token2:
    fosc.append(float((item[2:])))

print(energy,fosc)

#### Making histogram

bin_array=np.linspace(1.5,3.5,100)

newhist=[]
hist, bin_edges=np.histogram(energy,bins=bin_array)
for item in hist:
    newhist.append(item/max(hist))
    

spectra= plt.hist(energy,bins=bin_array)
#sns.distplot(energy, bins=bin_array, kde=True, hist=True, norm_hist=False, color="red")

plt.xlabel("Energy, eV")
plt.ylabel("Counts")

#plt.show()
fig=plt.figure()
#ax=plt.axes(projection='3d')
#ax.contour3D(energy,fosc, [])

### Making KDE
#kde=sts.gaussian_kde(energy)
#plt.plot(bin_array, kde.pdf(bin_array))
#plt.plot(bin_array[:-1], newhist)
plt.show()

# Resample the HISTOGRAM to find KDE 



