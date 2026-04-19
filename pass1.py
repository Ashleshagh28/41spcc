# INPUT PROGRAM (your given input)
source = [
    "START 100 - -",
    "- MOVER AREG ='5'",
    "- ADD BREG ='1'",
    "LOOP SUB CREG A",
    "- MOVER AREG ='2'",
    "- ADD BREG B",
    "- SUB DREG ='3'",
    "- MOVER BREG ='4'",
    "- ADD CREG ='6'",
    "A DS 1 -",
    "B DS 2 -",
    "- STOP - -",
    "END - - -"
]

symtab = {}
littab = {}

# MOT
mot = {
    "MOVER": 1,
    "ADD": 2,
    "SUB": 3,
    "MOVEM": 4,
    "STOP": 5
}

# POT
pot = {
    "START": 1,
    "END": 2,
    "DS": 3,
    "DC": 4
}

locctr = 0
start_addr = 0

print("INTERMEDIATE CODE")
print("--------------------------------")

for line in source:
    parts = line.replace(",", "").split()

    # Ensure 4 fields
    while len(parts) < 4:
        parts.append("-")

    label, opcode, op1, op2 = parts

    # START
    if label == "START":
        locctr = int(opcode)
        start_addr = locctr
        print(f"(AD,01) (C,{locctr})")
        continue

    # END
    if label == "END":
        print("(AD,02)")
        break

    # SYMBOL TABLE
    if label != "-":
        symtab[label] = locctr

    # LITERAL TABLE
    if op2.startswith("='"):
        if op2 not in littab:
            littab[op2] = None

    # DS
    if opcode == "DS":
        print(f"{locctr} (DL,01) (C,{op1})")
        locctr += int(op1)

    # DC
    elif opcode == "DC":
        print(f"{locctr} (DL,02) (C,{op1})")
        locctr += 1

    # STOP
    elif opcode == "STOP":
        print(f"{locctr} (IS,05)")
        locctr += 1

    # MACHINE INSTRUCTION
    else:
        print(f"{locctr} (IS,{mot.get(opcode,0):02d}) {op1} {op2}")
        locctr += 1


# ASSIGN LITERAL ADDRESSES
for lit in littab:
    littab[lit] = locctr
    locctr += 1

# OUTPUTS
print("\nSYMBOL TABLE")
print("Label\tAddress")
for k, v in symtab.items():
    print(k, "\t", v)

print("\nLITERAL TABLE")
print("Literal\tAddress")
for k, v in littab.items():
    print(k, "\t", v)

print("\nPROGRAM LENGTH =", locctr - start_addr)
