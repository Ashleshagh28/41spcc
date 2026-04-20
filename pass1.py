# INPUT PROGRAM
source = [
    "MACRO",
    "INCR &ARG",
    "MOVER AREG, &ARG",
    "ADD BREG, ='1'",
    "MEND",
    "MACRO",
    "SUM &A,&B",
    "ADD AREG, &A",
    "ADD BREG, &B",
    "MEND",
    "START 100",
    "INCR A",
    "SUM A,B",
    "END"
]

# TABLES
MNT = []
MDT = []
ALA = []

MNTC = 1
MDTC = 1

def line():
    print("-" * 50)

intermediate = []
i = 0

# PASS 1
while i < len(source):

    current = source[i].strip()

    if current == "":
        i += 1
        continue

    # MACRO START
    if current == "MACRO":

        i += 1
        header = source[i].strip()
        parts = header.split()

        # Identify macro name & arguments
        macro_name = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        # Add to MNT
        MNT.append((MNTC, macro_name, MDTC))
        MNTC += 1

        # Fill ALA
        ALA.clear()
        for arg in args:
            for a in arg.split(','):
                ALA.append(a.strip())

        # Store header in MDT
        MDT.append((MDTC, header))
        MDTC += 1

        i += 1

        # Read macro body
        while source[i].strip() != "MEND":

            body = source[i].strip()

            # Replace arguments with positional notation
            for index, arg in enumerate(ALA):
                body = body.replace(arg, f"#{index+1}")

            MDT.append((MDTC, body))
            MDTC += 1

            i += 1

        # Store MEND
        MDT.append((MDTC, "MEND"))
        MDTC += 1

    else:
        # Normal statements → Intermediate code
        intermediate.append(current)

    i += 1


# OUTPUT
print("\n===== PASS-1 OF TWO PASS MACRO PROCESSOR =====")

print("\nSOURCE PROGRAM:")
line()
for s in source:
    print(s)

print("\nINTERMEDIATE CODE:")
line()
for s in intermediate:
    print(s)

print("\nMNT (MACRO NAME TABLE):")
line()
print("Index\tMacro Name\tMDT Index")
for m in MNT:
    print(m[0], "\t", m[1], "\t\t", m[2])

print("\nMDT (MACRO DEFINITION TABLE):")
line()
print("Index\tCard")
for m in MDT:
    print(m[0], "\t", m[1])

print("\nALA (ARGUMENT LIST ARRAY):")
line()
print("Index\tArgument")
for i, a in enumerate(ALA, start=1):
    print(i, "\t", a)

print("\nCOUNTERS:")
line()
print("MNTC =", MNTC - 1)
print("MDTC =", MDTC - 1)
