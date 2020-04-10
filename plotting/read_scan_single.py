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

'''
    #files = os.listdir('./*data')
    #files.sort()
    #files=["scan11_360.data"]
    #constants Gromacs energy units kJ/mol
'''
kcalmolmm=0.238846 # 1kj/mol to kcal/mol 
kcalmolqm=627.509 # 1 kj/mol to kcal/mol

# number of scan (1,2,3,4,5) correspond to the flexible dihedral number in beta-carotene,
# counting flexible bonds from aroamtic ring
mm_data=['Scan1.dat', "Scan2.dat", "Scan3.dat", "Scan4.dat", "Scan5.dat"]
qm_data=["bcr_scan1.data", "bcr_scan2.data", "bcr_scan3.data","bcr_scan4.data", "bcr_scan5.data"]

def scan_extractor(qm,mm):
    '''
    Function that reads the energies of potential of a scan file
    '''
    print(qm)
    f=open(qm,"r")
    print(mm)
    f2=open(mm,"r")

    aux_coord=[] #x
    aux_coordinate_scaled=[]
    aux_energy=[]
    rel_energy=[] #y
## QM data, f

    lines=f.readlines()[4:]
    count=0
    for line in lines: # First set of data, -360
        columns=" ".join(line.split())
        aux_coord_x_single_value=float(columns.split(" ")[0])
        #if ((aux_coord_x_single_value >= -180.) & (aux_coord_x_single_value <= 180.)):
        aux_coord.append(aux_coord_x_single_value-360)
        aux_energy.append(float((columns.split(" ")[1])))
        aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0]) 
        count=count+1

    for line in lines: # Second set of data, 0
        columns=" ".join(line.split())
        aux_coord_x_single_value=float(columns.split(" ")[0])
        #if ((aux_coord_x_single_value >= -180.) & (aux_coord_x_single_value <= 180.)):
        aux_coord.append(aux_coord_x_single_value)
        aux_energy.append(float((columns.split(" ")[1])))
        aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0]) 
        count=count+1

    for line in lines: # Third set of data, +360
        columns=" ".join(line.split())
        aux_coord_x_single_value=float(columns.split(" ")[0])
        #if ((aux_coord_x_single_value >= -180.) & (aux_coord_x_single_value <= 180.)):
        aux_coord.append(aux_coord_x_single_value+360)
        aux_energy.append(float((columns.split(" ")[1])))
        aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0]) 
        count=count+1
    
    
    #if (qm == 'bcr_scan1.data'): # ! only because this scenario had this as difference, we repeat the previous loop
    #    for line in lines:
    #        columns=" ".join(line.split())
    #        aux_coord_x_single_value=float(columns.split(" ")[0])
    #        if ((aux_coord_x_single_value >= -180.) & (aux_coord_x_single_value <= 180.)):
    #            aux_coord.append(aux_coord_x_single_value)
    #            aux_energy.append(float((columns.split(" ")[1])))
    #            aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0]) 
    #            count=count+1
    for element in aux_energy:
        rel_energy.append((element-min(aux_energy))*kcalmolqm) # relative enrgy in kcal/mol

    plt.plot(aux_coord,rel_energy, label="QM", linestyle="-", color="black", linewidth=2)
    plt.legend(fontsize=15)

    '''
        #for element in (range(0, (scan_number-1),1)):
        #    print(element)
        #    print(aux_coord[])


        #for line in lines:
        #    columns=" ".join(line.split())
        #    aux_coord.append(float(columns.split(" ")[0]))
        #    aux_energy.append(float((columns.split(" ")[1])))
        #energy=(aux_energy[::-1])
        #print(aux_coord)
        #coordinate_scaled=(aux_coordinate_scaled[::-1]) 
        #energy=(aux_energy)
        #coordinate_scaled=(aux_coord) 


        ##Extending the graph for the interval -180 to 180, scaled scan coordinates
        #for element in range(len(coordinate_scaled)-1,-1, -1 ):
            #print(element)
        #    coordinate_scaled.append(coordinate_scaled[element])
            #energy.append(energy[element])
        #print(coordinate_scaled)
        #print(energy)
        ## Creating array with original coordinatel
        #for i in range(len(coordinate_scaled)):
        #    coordinate.append(coordinate_scaled[i]-aux_coord[0])
            #rel_energy.append(energy[i]-min(energy))

        #Extending the graph for the interval -180 to 180, scaled scan coordinates
    '''
    #### MM data
    aux_coord=[]
    aux_coordinate_scaled=[]
    aux_energy=[]
    rel_energy=[]

    lines=f2.readlines()[2:]
    count=0
    for line in lines:
        columns=" ".join(line.split())
        aux_coord.append(float(columns.split(" ")[0]))
        aux_energy.append(float((columns.split(" ")[1])))
        aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0]) 
        count=count+1
    for element in aux_energy:
        rel_energy.append((element-min(aux_energy))*kcalmolmm) # relative enrgy in kcal/mol

    
    plt.plot(aux_coord,rel_energy, label="MM (GAFF)", linestyle="-.", color="black", linewidth=2)
    plt.legend(fontsize=15)
    #plt.plot()


    # Plot parameters
    plt.grid(True)
    plt.ylabel('Rel. Energy, kcal mol$^{-1}$',fontsize=15) #plt.ylabel
    plt.xlabel("Dihedral angle" + r" $\theta$, " +"Scan " + str(qm[8:-5]), fontsize=15)
    #plt.yticks(fontsize=10)  
    plt.yticks((np.linspace(min(rel_energy), max(rel_energy), 5)), fontsize=15)  
    plt.xticks(fontsize=15)  
    plt.xlim(-180,180)
    plt.tight_layout()
    plt.savefig(qm+"scan.eps")
    plt.close('all')

#
for n in range(5):
    scan_extractor(qm_data[n],mm_data[n])

#qmscan_extractor(file)
