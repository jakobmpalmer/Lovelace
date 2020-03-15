def NAND(A, B):
    nand = 1
    
    if A > 1 or B > 1:
        print("Invalid Input")
        return

    if A and B == 1:
        nand = 0
    return nand

print("(0, 1) \treturn: " + str(NAND(0, 1)))
print("(0, 0) \treturn: " + str(NAND(0, 0)))
print("(1, 0) \treturn: " + str(NAND(1, 0)))
print("(1, 1) \treturn: " + str(NAND(1, 1)))

print("\n")
print("(2, 1) \treturn: " + str(NAND(2,1)))
print("(1, 2) \treturn: " + str(NAND(1,2)))
print("\nEND")