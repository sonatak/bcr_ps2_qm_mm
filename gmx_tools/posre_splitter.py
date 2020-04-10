all_h_pdb = open('allH.pdb', 'r')
posre_itp = open('posre.itp', 'r').read().split('\n')

pdb_line_start_pointer=0
pdb_line_pointer=0
previous_chain_id=''
chain_id=''
pdb_line_splits=[]
chain_names=[]
chain_elements=[]
pdb_line_splits_pointer=1
posre_atom_numbers=[]

#Cycle to read all atom numbers in posre.itp file:
posre_line_pointer=0
for posre_line in posre_itp:
    if(posre_line_pointer>1):
        posre_atom_numbers.append(int(posre_line[0:6]))
    posre_line_pointer+=1

#Cycles to read allH.pdb file, calculate starting line of chain and find chain name 
for pdb_line in all_h_pdb:
    if (pdb_line_pointer > 0):
        previous_chain_id = chain_id
    chain_id = pdb_line[21]
    pdb_line_pointer+=1
    if ((pdb_line_pointer > 0) & (previous_chain_id!=chain_id)): # != not equal

        chain_names.append(chain_id)
        
        chain_elements.append(pdb_line_pointer)
        posre_split_filename= 'posre_Protein_chain_' + chain_id + '.itp'
        f=open(posre_split_filename, "w")
        f.close()
print(chain_names)


count=0
for i in (chain_names):
    begin_chain_line_numb=chain_elements[count]
    count=count+1
    final_chain_line_numb=chain_elements[count]-1
    print(begin_chain_line_numb,final_chain_line_numb , i)
    x=0
    posre_split_filename= 'posre_Protein_chain_' + i + '.itp'
    f=open(posre_split_filename, "a")
    f.write("[ position restraints ]"+"\n"+ ";   i   func   fcx  fcy  fcz" + "\n")
    #Writing posre files
    for x in posre_atom_numbers:
        if ( begin_chain_line_numb <= x < final_chain_line_numb  ):
            substracted_index=x-begin_chain_line_numb+1
            #print(substracted_index)
            f=open(posre_split_filename, "a")
            f.write(str(substracted_index )+ "  1  "  + " 1000 " +" 1000 " " 1000 " +"\n" )


# loop for last chain
for x in posre_atom_numbers:
        if (80851  <= x < 81812  ):
            substracted_index=x-+1
            #print(substracted_index)
            f=open("xxxx", "a")
            f.write(str(substracted_index )+ "  1  "  + " 1000 " +" 1000 " " 1000 " +"\n" )






#print(pdb_line_splits)
#print('Loaded neccesary splits ('+len(pdb_line_splits)+'), splitting files...')
#for posre_line in range(2, len(posre_itp), 1):
#    posre_split_data = ["[ position_restraints ]\n;  i funct       fcx\
#        fcy        fcz"]
#    if(posre_line==pdb_line_splits[pdb_line_splits_pointer]["pdb_line_start_pointer"]):
#        posre_split_data.append(posre_itp[pdb_line_splits[pdb_line_splits_pointer-1]["pdb_line_start_pointer"]:posre_line])
#        posre_split_filename = open(
#            'posre_Protein_chain_' + pdb_line_splits[pdb_line_splits_pointer]["previous_chain_id"] + '.itp', 'w'
#        )
#        for posre_split_line in posre_split_data:
#            posre_split_filename.write("%s\n" % posre_split_line)
#        pdb_line_splits_pointer+=1
#print('itp file splitted')
