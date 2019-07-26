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
    for i in periodic_table:
        print (i, periodic_table[i])

    
    
def molecular_mass(chemical_formula):
    mass = 0
    indiv_chemicals = re.findall('[A-Z][^A-Z]*', chemical_formula) #data prep    
    for chem in indiv_chemicals:
        print("chem= " + chem)
        print(periodic_table.get(str(chem)))
        mass += float(periodic_table.get(chem)) #add mass
        #chemical_formula.replace(row[0], "")#remove chemical
        #print("Uncalculated molocules= " + chemical_formula)
        print("Molecular mass is " + str(mass) + " amu.")
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
            
    print("Molecular mass is " + str(mass) + " amu.")
    return mass

print("TEST: Pa")
molecular_mass("Pa")
print("TEST: OCS")
molecular_mass("OCS")
print("TEST: C4H4AsH")
molecular_mass("C4H4AsH")
print("TEST: C20H25N3O")
molecular_mass("C20H25N3O")

