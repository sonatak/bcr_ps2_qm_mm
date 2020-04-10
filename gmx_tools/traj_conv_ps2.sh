# produce the trajout.pdb
gmx trjconv -f  equil50.xtc -o qmmm_inp/trajout.pdb -s equil50.tpr  -sep -b 0 -e 2000 -skip 1
#produce the index files for snapshot
gmx select -f ./qmmm_inp/trajout1.pdb  -sf selection_single.dat -s minim.gro -on ./qmmm_inp/index1.ndx
gmx trjconv -f ./qmmm_inp/trajout1.pdb -s minim.gro  -o ./qmmm_inp/sphere1.gro -n ./qmmm_inp/index1.ndx -center -pbc mol

