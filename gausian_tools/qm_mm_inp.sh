#!/bin/bash

for i in `seq 1 50`
do
sed -i '/C /s/$/ -0.302700/'  sphere$i.xyz
sed -i '/Cl /s/$/ 0.30060/'  sphere$i.xyz
sed -i  '/H /s/$/ 0.00070/'  sphere$i.xyz

sed -i '3s/-0.302700// ' sphere$i.xyz
sed -i '5s/-0.302700// ' sphere$i.xyz
sed -i '7s/-0.302700// ' sphere$i.xyz
sed -i '10s/-0.302700// ' sphere$i.xyz

sed -i '4s/0.00070//  ' sphere$i.xyz
sed -i '6s/0.00070//  ' sphere$i.xyz
sed -i '8s/0.00070//  ' sphere$i.xyz
sed -i '9s/0.00070//  ' sphere$i.xyz
sed -i '11s/0.00070//  ' sphere$i.xyz
sed -i '11s/0.00070//  ' sphere$i.xyz

done

#if  grep -q "Cl" sphere0.xyz ; then
#   grep -n "Cl"  sphere0.xyz | gawk '{print $1}' FS=":" > cl_index_sphere.dat
#fi

#if  grep -q "C " sphere0.xyz ; then
#   grep -n "C "  sphere0.xyz | gawk '{print $1}' FS=":" > c_index_sphere.dat
#fi


#if  grep -q "H " sphere0.xyz ; then
 #  grep -n "H "  sphere0.xyz | gawk '{print $1}' FS=":" > h_index_sphere.dat
#fi

