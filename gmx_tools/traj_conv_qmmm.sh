#!/bin/bash
#module load gromacs

echo 'Enter name of trajectory file .xtc, trr '
read traj
echo 'Enter name of tpr file '
read tprfile
#echo 'Enter the step of reading coordinates from trajectory .xtc file. Binary snapshots will be converted into .pdb files'  
#read step
#echo 'Enter the number of snapshots to be written'
#read trajout

#end = trajout*step
mkdir qmmm_inp


echo 'Converting .trr to pdb ..............'
#gmx_d trjconv -f $traj -o qmmm_inp/trajout.pdb -center -pbc mol -s $tprfile -sep -b 0 -e 2000 -skip 50
#trjconv_d -f prod.trr -o qmmm_inp/trajout.pdb -s prod.tpr -sep -skip 10
#echo 'Converting pdb to xyz..............'

for i in `seq 0 200`
do

# Important! Concert tpr to g96 before the running select! For compatibility
# Generating ndx files
#gmx select -f ./qmmm_inp/trajout$i.pdb -sf selection.dat -s prod.g96 -on ./qmmm_inp/index$i.ndx 	
# Writing out spheres in gro format
#gmx trjconv -f ./qmmm_inp/trajout$i.pdb -s prod.g96 -o ./qmmm_inp/sphere$i.gro -n ./qmmm_inp/index$i.ndx -center -pbc mol
# Writing out spheres with xyz format
babel ./qmmm_inp/sphere$i.gro ./qmmm_inp/sphere$i.xyz 
done
# Adding point charges to MM part of xyz file

for i in `seq 0 200`
do
#seperate qm part
head -n 98 qmmm_inp/sphere$i.xyz | tail -n 96 > qmmm_inp/qmpart$i.xyz
#leaving mm part
sed '1,98d' qmmm_inp/sphere$i.xyz > qmmm_inp/mmpart$i.xyz
done


for i in `seq 1 200`
do
sed -i '/O /s/$/ -0.834/'  qmmm_inp/mmpart$i.xyz
sed -i '/H /s/$/ 0.417/'  qmmm_inp/mmpart$i.xyz
done

# Take out ato names in MM part
for i in `seq 3 200`
do
	sed -i "s/^..//" qmmm_inp/mmpart$i.xyz
done
cd qmmm_inp


for i in `seq 1 200`
do
echo "%chk=traj$i.chk" > snapshot$i.com
echo "%Mem = 4GB" >> snapshot$i.com
echo "%nproc=8" >> snapshot$i.com
echo "# b3lyp/6-31g* td(root=1) charge" >> snapshot$i.com
echo "" >> snapshot$i.com
echo "BCR+water tddft $numb" >> snapshot$i.com
echo "" >> snapshot$i.com
echo "0 1" >> snapshot$i.com
cat qmpart$i.xyz >> snapshot$i.com
echo '' >> snapshot$i.com
cat mmpart$i.xyz >> snapshot$i.com
echo "" >> snapshot$i.com
done

#Removing the files

#rm qmmm_inp/*gro
rm trajout*
rm index*
rm *#*
rm *xyz



