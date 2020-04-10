import os 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot
import scipy.stats as sts
from mpl_toolkits import mplot3d
from scipy.stats import norm

#### Reading data

snapshots = os.listdir('./gas_phase/data/')
snapshots1 = os.listdir('./water/data/')
td_spectra="spec_LS_TD.dat"
experimental="bcr_RT_exp_Jailaubekov.dat"

token=[]
token2=[]
energy=[]
fosc=[]

 # Experimental data in 3-methylpentane Jailaubekov
f=open(experimental, "r")
energy_exp=[]
intensity_exp=[]

lines = f.readlines()
count = 0
for line in lines:  # First set of data, -360
   # columns =line.split()
    energy_exp.append(float(line.split(" ")[0]))
    intensity_exp.append(float(line.split(" ")[1]))

 # MD simulation data gas pahse

for snapshot in snapshots:
    f=open(str("./gas_phase/data/"+snapshot),"r")
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

token=[]
token2=[]
energy1=[]
fosc1=[]

 # MD simulation data in water

for snapshot in snapshots1:
    f=open(str("./water/data/"+snapshot),"r")
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
    energy1.append(float(item))
for item in token2:
    fosc1.append(float((item[2:])))


#print("sum noem energy" )
## Reading QM data from LS TD spectra

f=open(td_spectra, "r")
energy_fcc=[]
intensity=[]

lines = f.readlines()
count = 0
for line in lines:  # First set of data, -360
    columns = " ".join(line.split())
    energy_fcc.append(float(columns.split(" ")[0]))
    intensity.append(float(columns.split(" ")[1]))

#Normalizing the QM LS data

sum_intensity=sum(intensity)
norm_intensity=[]
norm_intensity_aux=[]
mu1_list=[]
mu2_list=[]

#calculate the statistical data mu1 and mu2 of TD LS
for element in intensity:
    norm_intensity.append(element/max(intensity))

for x in range(len(intensity)):
    value=intensity[x]*energy_fcc[x]
    mu1_list.append(value)
    mu2_list.append(intensity[x]*energy_fcc[x]*energy_fcc[x])

mu1=sum(mu1_list)/sum(intensity)
print("mu1,",mu1)
mu2=sum(mu2_list)/sum(intensity)
print("mu2", mu2)
sigma=np.sqrt(mu2-(mu1**2))
print("sigma", sigma)
print("sum intensity", sum(norm_intensity))

#calculate the statistical data mu1 and mu2 of experimental spectra
mu1_list=[]
mu2_list=[]

for x in range(len(energy_exp)):
    value=intensity_exp[x]*energy_exp[x]
    mu1_list.append(value)
    mu2_list.append(intensity_exp[x]*energy_exp[x]*energy_exp[x])

mu1wat=sum(mu1_list)/sum(intensity_exp)
print("mu1wat,",mu1wat)
mu2wat=sum(mu2_list)/sum(intensity_exp)
print("mu2wat", mu2wat)
sigmawat=np.sqrt(mu2wat-(mu1wat**2))
print("sigmawat", sigmawat)


plt.plot(energy_fcc, norm_intensity, linewidth=2,label="TD $\mu$ = %.2f,  $\sigma$ = %.2f" % (mu1, sigma), color="grey")

#### Getting normal distribution
mu1,std1 = norm.fit(energy1) # in water MD

mu, std = norm.fit(energy) # in fas gas phase MD 

nameexp = "Exp$^{[1]}$, $\mu$ = %.2f,  $\sigma$ = %.2f" % (mu1wat, sigmawat) 
plt.plot(energy_exp, intensity_exp, linewidth=2,label=nameexp, color="black")

xmin=1.0
xmax=3.25

x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
p1=norm.pdf(x,mu1,std1)
p_aux1=p1/max(p1)
p_aux=p/max(p) # max normalized to 1
name = "MD$^{[2]}$, $\mu$ = %.2f,  $\sigma$ = %.2f" % (mu, std)
namewat = "MD$^{[3]}$, $\mu$ = %.2f,  $\sigma$ = %.2f" % (mu1, std1) 
plt.xlim(xmin,xmax)
plt.yticks(fontsize=15)
plt.xticks(fontsize=15)
plt.plot(x, p_aux, 'k', linewidth=2,label=name, color="black", linestyle="dotted") # Gas phase
plt.plot(x, p_aux1, 'k', linewidth=2,label=namewat, color="grey", linestyle="dashed") # Water
plt.xlabel("Energy, eV",fontsize=15)
plt.ylabel("Normalized lineshape", fontsize=15)
plt.legend(loc="upper left",fontsize=15)
plt.text(3.1, 0.9, 'T=300K',fontsize=15, horizontalalignment='center', verticalalignment='center')
plt.grid(True)
plt.show()





