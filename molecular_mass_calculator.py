####################################################################
# https://projectlovelace.net/problems/molecular-mass-calculator/  #
#                                                                  #
#  @uthor jakobmp                                                  #
#  7 / 25 / 2019                                                   #
####################################################################

import csv
import re


periodic_table = {}

with open('data/periodic_table.csv', newline='') as csvfile:
    periodic_table_reader = csv.reader(csvfile, delimiter=',')    
    for row in periodic_table_reader:
        tempEntry = { 
            row[0] : row[1] 
        }            
        periodic_table.update(tempEntry)    
    #for i in periodic_table:
        #print (i, periodic_table[i])

    
    
def molecular_mass(chemical_formula):
    mass = 0    
    
    indiv_chemicals = re.findall('[A-Z][^A-Z]*', chemical_formula) #data prep          
    for chem in indiv_chemicals:
        quant = 1
        chem_sum = 0
        quant_str = ""
        quant_str = chem

        for char in chem:            
            if(not char.isdigit()): #If char is a digit, remove the digits from the chem and set quant to digits                
                print("Letter == " + char)                
                quant_str = quant_str.replace(char, '')            
                print("AFTER REPLACED:: " + quant_str)
        for char in chem:
            if((quant_str).isdigit()):
                quant = int(quant_str)
                if(char.isdigit()): #If char is a digit, remove the digits from the chem and set quant to digits                
                    #print("char== " + char)
                    #quant = int(char)
                    chem = chem.replace(char, '')            
                    #print("CHEM:: " + chem)                                                        
        print("there are " + str(quant) + " of " + chem)
        print("Original Weight " + str(periodic_table.get(str(chem))))
        chem_sum = float(periodic_table.get(chem)) #add mass  
        chem_sum = chem_sum * quant
        print("Total Chem Weight= " + str(chem_sum))
        mass += chem_sum      
    
    mass = round(mass, 2)            
    print("Molecular mass of " + chemical_formula + " is " + str(mass) + " amu.")
    return mass 






def my_molecular_mass(chemical_formula):
    mass = 0
    
    with open('data/periodic_table.csv', newline='') as csvfile:
        periodic_table_reader = csv.reader(csvfile, delimiter=',')
        for row in periodic_table_reader:
            #print(", ".join(row))
            
            if(chemical_formula.find(row[0]) != None): #if current chem is in chem_form
                print("adding mass of " + row[0])
                mass+= row[1] #add mass
                chemical_formula.replace(row[0], "")#remove chemical
                print("Uncalculated molocules= " + chemical_formula)

    mass = round(mass, 2)            
    print("Molecular mass of " + chemical_formula + " is " + str(mass) + " amu.")
    return mass



print("\n\tTEST: Pa (231.04)")
molecular_mass("Pa") # 231.04
print("\n\tTEST: OCS (60.08)")
molecular_mass("OCS") # 60.08
print("\n\tTEST: C4H4AsH (128.00)")
molecular_mass("C4H4AsH") # 128.00
print("\n\tTEST: C20H25N3O (323.44)")
molecular_mass("C20H25N3O") # 323.44

