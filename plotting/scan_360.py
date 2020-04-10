'''
Program to read the energies of potential energy scan of 5 files
and assign it to their variables for further use in representations
'''
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot
import scipy.stats as sts
import re
from mpl_toolkits import mplot3d

#files = os.listdir('./*data')
#files.sort()
#files=["scan11_360.data"]
#constants
kcalmol=627.509 # 1ha to kcal/mol 


files=["bcr_scan1.data", "bcr_scan2.data", "bcr_scan3.data", "bcr_scan4.data","bcr_scan5.data"]

def qmscan_extractor(filename):
    '''
    Function that reads the energies of potential of a scan file
    '''
    print(filename)
    f=open(filename,"r")

    aux_coord=[]
    aux_coordinate_scaled=[]
    aux_energy=[]
    rel_energy=[]

    lines=f.readlines()[4:]
    count=0
    for line in lines:
        columns=" ".join(line.split())
        aux_coord.append(float(columns.split(" ")[0]))
        aux_energy.append(float((columns.split(" ")[1])))
        aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0]) 
        count=count+1
    for element in aux_energy:
        rel_energy.append((element-min(aux_energy))*kcalmol) # relative enrgy in kcal/mol

        
    # Rescaling x axis, if there are values higher than 360 degrees
    if (max(aux_coord) > 360.):
        aux_coord=np.array(aux_coord)
        aux_coord=aux_coord-360.    
    
    print((aux_coord))
    print(len(aux_energy))

    #plotting
    plt.plot(aux_coord,rel_energy)
    # Plot parameters
    plt.grid(True)
    plt.ylabel('Rel. Energy, kcal mol$^{-1}$',fontsize=12) #plt.ylabel
    plt.xlabel("Dihedral angle" + r" $\theta$, " +"Scan " + str(filename[8:-5]), fontsize=12)
    plt.yticks(fontsize=10)  
    plt.yticks((np.linspace(min(rel_energy), max(rel_energy), 5)), fontsize=10)  
    plt.xticks(fontsize=10)  
    plt.tight_layout()
    plt.savefig(file+"scan.eps")
    plt.close('all')

#
for file in files:
    qmscan_extractor(file)
#qmscan_extractor(file)
