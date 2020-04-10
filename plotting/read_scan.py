'''
Program to read the energies of potential energy scan of 5 files
and assign it to their variables for further use in representations
'''
import os
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sts
import re
from mpl_toolkits import mplot3d

'''
    #files = os.listdir('./*data')
    #files.sort()
    #files=["scan11_360.data"]
    #constants Gromacs energy units kJ/mol
'''
kcalmolmm = 0.238846  # 1kj/mol to kcal/mol
kcalmolqm = 627.509  # 1 kj/mol to kcal/mol

# number of scan (1,2,3,4,5) correspond to the flexible dihedral number in beta-carotene,
# counting flexible bonds from aroamtic ring
mm_data = ["Scan2.dat", "Scan3.dat", "Scan4.dat", "Scan5.dat"]
qm_data = ["bcr_scan2.data", "bcr_scan3.data",
           "bcr_scan4.data", "bcr_scan5.data"]
colors=["black", "grey", "purple", "orange"]


# PLot size of figure
plt.figure(figsize=(12, 6))


def scan_extractor(qm, mm, n):
    '''
    Function that reads the energies of a scan file
    '''
    print(qm)
    f = open(qm, "r")
    print(mm)
    f2 = open(mm, "r")


# QM data, f

    aux_coord_qm = []  # x
    #aux_coordinate_scaled = []
    aux_energy_qm = []
    rel_energy_qm = []  # y

    lines = f.readlines()[4:]
    count = 0
    for line in lines:  # First set of data, -360
        columns = " ".join(line.split())
        aux_coord_x_single_value = float(columns.split(" ")[0])
        # if ((aux_coord_x_single_value >= -180.) & (aux_coord_x_single_value <= 180.)):
        aux_coord_qm.append(aux_coord_x_single_value-360)
        aux_energy_qm.append(float((columns.split(" ")[1])))
        #aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0])
        count = count+1

    for line in lines:  # Second set of data, 0
        columns = " ".join(line.split())
        aux_coord_x_single_value = float(columns.split(" ")[0])
        # if ((aux_coord_x_single_value >= -180.) & (aux_coord_x_single_value <= 180.)):
        aux_coord_qm.append(aux_coord_x_single_value)
        aux_energy_qm.append(float((columns.split(" ")[1])))
        #aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0])
        count = count+1

    for line in lines:  # Third set of data, +360
        columns = " ".join(line.split())
        aux_coord_x_single_value = float(columns.split(" ")[0])
        # if ((aux_coord_x_single_value >= -180.) & (aux_coord_x_single_value <= 180.)):
        aux_coord_qm.append(aux_coord_x_single_value+360)
        aux_energy_qm.append(float((columns.split(" ")[1])))
        #aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0])
        count = count+1

    for element in aux_energy_qm:
        # relative enrgy in kcal/mol
        rel_energy_qm.append((element-min(aux_energy_qm))*kcalmolqm)

    # MM data

    aux_coord_mm = []
    aux_coordinate_scaled = []
    aux_energy_mm = []
    rel_energy_mm = []

    lines = f2.readlines()[2:]
    count = 0
    for line in lines:
        columns = " ".join(line.split())
        aux_coord_mm.append(float(columns.split(" ")[0]))
        aux_energy_mm.append(float((columns.split(" ")[1])))
        #aux_coordinate_scaled.append(-aux_coord[count]+aux_coord[0])
        count = count+1
    for element in aux_energy_mm:
        # relative enrgy in kcal/mol
        rel_energy_mm.append((element-min(aux_energy_mm))*kcalmolmm)

    plt.plot(aux_coord_qm, rel_energy_qm, label=("QM, scan " + str(m)),
             linestyle="-", color=colors[n], linewidth=2)
    plt.plot(aux_coord_mm, rel_energy_mm, label=("GAFF, scan " + str(m)),
             linestyle="-.", color=colors[n], linewidth=2)

   
    # Plot parameters
    plt.legend(fontsize=15, bbox_to_anchor=(1, 0.5), loc='center left')
    plt.grid(True)
    plt.ylabel('Rel. Energy, kcal mol$^{-1}$', fontsize=15)  # plt.ylabel
    plt.xlabel("Dihedral angle" + r" $\theta$, ", fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(np.arange(0, 11.5, step=2),fontsize=15)
    plt.xlim(-180, 180)
    plt.ylim(0, 11.5)
    plt.tight_layout()
    # plt.savefig(qm+"scan.eps",)
    # plt.close('all')




for n in range(4):
    m = n+2
    scan_extractor(qm_data[n], mm_data[n],n)
    

plt.show()
