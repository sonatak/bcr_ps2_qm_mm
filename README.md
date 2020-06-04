

# MASTER THESIS SCRIPTS
## Repository contains python and shell scrips in order to perform different tasks for molecular modelling and data analysis.


The scripts are used to solve following tasks in half-automated way:
1. Data analysis
* Python scripts to fit dihedral-bonds; dihedral-angle coupling terms with QM data using expanded *sin* superposition 
2. Gaussian tools
* Script to write multiple Gaussian input files (from multiple .xyz format snapshots)
* Script to  write multiple Gaussian QM/MM input files (from multiple .xyz format snapshots) using point charges of surroundings 
3. Plotting data
* Python scripts to read data and plot QM and MM energy scans for dihedrals.  
* Python scripts to read data and plot absorbtion spectra calculated from distribution of vertical energies calculated from MD simulation snapshots. Calculating statistical parameters, getting normal distribution of spectra.
4. Gromacs (gmx) tools
* Script to split Single posre.itp file into multiple posre files for each protein chain, restraining backbone atoms
* Scripts to write snapshots from simulation trajectory and write Gaussian inputs.

## Author
Sonata Kvedaravičiūtė
