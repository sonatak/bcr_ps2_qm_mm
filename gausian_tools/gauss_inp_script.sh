#!/bin/bash
echo 'Enter number of files'
read numb
for i in `seq 1 $numb`
do 
#echo "%chk=./traj$numb.chk" > qmmm_inp/snapshot$i.com
echo "%Mem = 2GB" >> qmmm_inp/snapshot$i.com
echo "%nproc=16" >> qmmm_inp/snapshot$i.com
echo "# b3lyp/6-31g* td " >> qmmm_inp/snapshot$i.com
echo "" >> qmmm_inp/snapshot$i.com
echo "Butadiene tddft $numb" >> qmmm_inp/snapshot$i.com
echo "" >> qmmm_inp/snapshot$i.com
echo "0 1" >> qmmm_inp/snapshot$i.com
tail -n +3 qmmm_inp/sphere$i.xyz >> qmmm_inp/snapshot$i.com




echo '' >> qmmm_inp/snapshot$i.com
done
