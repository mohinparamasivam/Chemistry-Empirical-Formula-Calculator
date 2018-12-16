
#!/usr/bin/ env python3

print("                                                                       ")
print("                                                                       ")
print ("            #################################################" )       
print ("            #                                               #" )        
print ("            #       Chemistry Empirical Formula Calculator  #" )        
print ("            #                                               #" )        
print ("            #                  Version 1.0                  #" )        
print ("            #                                               #" )       
print ("            #           Author : Mohin Paramasivam          #" )       
print ("            #                                               #" )       
print ("            #################################################" )       

print("                                                                   ")


print("                                           ")



Atom1 = input("Please enter the 1st atom symbol  : ")
mass_Atom1 = float(input("Please enter the mass of atom " + Atom1 + " = "))
Relative_atomic_mass1 = float(input("Please enter the relative atomic mass of " + Atom1 + " ="))

print("													")

Atom2 = input("Please enter the 2nd atom symbol : ")
mass_Atom2 = float(input("Please enter the mass of atom " + Atom2 + " = "))
Relative_atomic_mass2 = float(input("Please enter the relative atomic mass of " + Atom2 + " ="))

print("													")

check_3rd_atom = input(" Is there any 3rd atom ? ( Yes / No ) ")

print("													")

if((check_3rd_atom=="Yes") or (check_3rd_atom=="yes") or (check_3rd_atom=="YES")):
	Atom3 = input("Please enter the third atom symbol : ")
	mass_Atom3 = float(input("Please enter the mass of atom " + Atom3 + " = "))
	Relative_atomic_mass3 =  float(input("Please enter the relative atomic mass of " + Atom3 + " ="))


	mol_atom1 = mass_Atom1/Relative_atomic_mass1
	mol_atom1_int = int(round(mol_atom1) - .5) + (mol_atom1 > 0)



	mol_atom2 = mass_Atom2/Relative_atomic_mass2
	mol_atom2_int = int(round(mol_atom2) - .5) + (mol_atom2 > 0)


	mol_atom3 = mass_Atom3/Relative_atomic_mass3
	mol_atom3_int = int(round(mol_atom3) - .5) + (mol_atom3 > 0)


	if((mol_atom1_int) < (mol_atom2_int)) and ((mol_atom1_int)<(mol_atom3_int)):
		ratio_atom1 = mol_atom1_int/mol_atom1_int
		ratio_atom2 = mol_atom2_int/mol_atom1_int
		ratio_atom3 = mol_atom3_int/mol_atom1_int

	elif((mol_atom2_int)<(mol_atom1_int)) and ((mol_atom2_int)<(mol_atom3_int)):
			ratio_atom1 = mol_atom1_int/mol_atom2_int
			ratio_atom2 = mol_atom2_int/mol_atom2_int
			ratio_atom3 = mol_atom3_int/mol_atom2

	elif((mol_atom3_int)<(mol_atom1_int)) and ((mol_atom3_int)<(mol_atom2)):
		ratio_atom1 = mol_atom1_int/mol_atom3_int
		ratio_atom2 = mol_atom2_int/mol_atom3_int
		ratio_atom3 = mol_atom3_int/mol_atom3_int

	elif((mol_atom1_int) == (mol_atom2_int)) and ((mol_atom1_int)<(mol_atom3_int)):
		ratio_atom1 = mol_atom1_int/mol_atom1_int
		ratio_atom2 = mol_atom2_int/mol_atom1_int
		ratio_atom3 = mol_atom3_int/mol_atom1_int

	elif((mol_atom1_int) == (mol_atom2_int)) and ((mol_atom3_int)<(mol_atom1_int)):
		ratio_atom1 = mol_atom1_int/mol_atom3_int
		ratio_atom2 = mol_atom2_int/mol_atom3_int
		ratio_atom3 = mol_atom3_int/mol_atom3_int

	elif((mol_atom1_int) == (mol_atom3_int)) and ((mol_atom1_int)<(mol_atom2_int)):
		ratio_atom1 = mol_atom1_int/mol_atom1_int
		ratio_atom2 = mol_atom2_int/mol_atom1_int
		ratio_atom3 = mol_atom3_int/mol_atom1_int

	elif((mol_atom1_int) == (mol_atom3_int)) and ((mol_atom2_int)<(mol_atom1_int)):
		ratio_atom1 = mol_atom1_int/mol_atom2_int
		ratio_atom2 = mol_atom2_int/mol_atom2_int
		ratio_atom3 = mol_atom3_int/mol_atom2_int

	elif((mol_atom2_int) == (mol_atom3_int)) and ((mol_atom1_int)<(mol_atom3_int)):
		ratio_atom1 = mol_atom1_int/mol_atom1_int
		ratio_atom2 = mol_atom2_int/mol_atom1_int
		ratio_atom3 = mol_atom3_int/mol_atom1_int

	elif((mol_atom2_int) == (mol_atom3_int)) and ((mol_atom3_int)<(mol_atom1_int)):
		ratio_atom1 = mol_atom1_int/mol_atom3_int
		ratio_atom2 = mol_atom2_int/mol_atom3_int
		ratio_atom3 = mol_atom3_int/mol_atom3_int






	ratio_atom1_int =int(round(ratio_atom1) - .5) + (ratio_atom1 > 0)
	ratio_atom2_int =int(round(ratio_atom2) - .5) + (ratio_atom2 > 0)
	ratio_atom3_int =int(round(ratio_atom3) - .5) + (ratio_atom3 > 0)





	print(" The Empirical Formula : " + str(Atom1)+str(ratio_atom1_int)+str(Atom2)+str(ratio_atom2_int)+str(Atom3)+str(ratio_atom3_int))

else:

	mol_atom1 = mass_Atom1/Relative_atomic_mass1
	

	mol_atom2 = mass_Atom2/Relative_atomic_mass2


	if((mol_atom1) < (mol_atom2)):
		ratio_atom1 =(mol_atom1/mol_atom1)
		ratio_atom2 =(mol_atom2/mol_atom1)
		
	elif((mol_atom2)<(mol_atom1)):
			ratio_atom1 =(mol_atom1/mol_atom2)
			ratio_atom2 = (mol_atom2/mol_atom2)
			
	else:
		ratio_atom1 = (mol_atom1/mol_atom1)
		ratio_atom2 =( mol_atom2/mol_atom2)



	ratio_atom1_int = int(ratio_atom1)
	ratio_atom2_int = int(ratio_atom2)

	if(ratio_atom1_int==1 and ratio_atom2_int==1):
		ratio_atom1_final = ratio_atom1*2
		ratio_atom2_final = ratio_atom2*2
		ratio_atom1_perfect =int(round(ratio_atom1_final) - .5) + (ratio_atom1_final > 0)
		ratio_atom2_perfect =int(round(ratio_atom2_final) - .5) + (ratio_atom2_final > 0)
		print(" Empirical Formula : " + str(Atom1)+ str(ratio_atom1_perfect)+" "+ str(Atom2)+str(ratio_atom2_perfect))
	else:
		ratio_atom1_perfect =int(round(ratio_atom1) - .5) + (ratio_atom1 > 0)
		ratio_atom2_perfect =int(round(ratio_atom2) - .5) + (ratio_atom2 > 0)
		print(" Empirical Formula : " + str(Atom1)+ str(ratio_atom1_perfect)+" " + str(Atom2)+str(ratio_atom2_perfect))



