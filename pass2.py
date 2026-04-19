# SAME INPUT PROGRAM
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

# FROM PASS-1
symtab = {
    "LOOP": 102,
    "A": 109,
    "B": 110
}

littab = {
    "='5'": 111,
    "='1'": 112,
    "='2'": 113,
    "='3'": 114,
    "='4'": 115,
    "='6'": 116
}

# OPCODES
mot = {
    "MOVER": "01",
    "ADD": "02",
    "SUB": "03",
    "MOVEM": "04",
    "STOP": "00"
}

# REGISTER CODES
reg = {
    "AREG": "1",
    "BREG": "2",
    "CREG": "3",
    "DREG": "4"
}

locctr = 0

print("\nPASS-2 OUTPUT (OBJECT CODE)")
print("--------------------------------")

for line in source:
    parts = line.replace(",", "").split()

    while len(parts) < 4:
        parts.append("-")

    label, opcode, op1, op2 = parts

    # START
    if label == "START":
        locctr = int(opcode)
        continue

    # END
    if label == "END":
        break

    # MACHINE INSTRUCTIONS
    if opcode in mot:

        opcode_val = mot[opcode]
        reg_val = reg.get(op1, "0")

        # ADDRESS RESOLUTION
        if op2.startswith("='"):
            addr = littab.get(op2, 0)
        elif op2 in symtab:
            addr = symtab[op2]
        else:
            addr = "000"

        print(f"{locctr} -> {opcode_val} {reg_val} {addr}")
        locctr += 1

    # DS (no machine code)
    elif opcode == "DS":
        locctr += int(op1)

    # DC
    elif opcode == "DC":
        print(f"{locctr} -> 00 0 {op1}")
        locctr += 1

    # STOP
    elif opcode == "STOP":
        print(f"{locctr} -> 00 0 000")
        locctr += 1


# PRINT SYMBOL TABLE
print("\nSYMBOL TABLE")
print("--------------------")
print("Label\tAddress")
for k, v in symtab.items():
    print(f"{k}\t{v}")

# PRINT LITERAL TABLE
print("\nLITERAL TABLE")
print("--------------------")
print("Literal\tAddress")
for k, v in littab.items():
    print(f"{k}\t{v}")
