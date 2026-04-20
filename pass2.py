# Using data from Pass-1 (same example)

# MNT: (Index, Macro Name, MDT Index)
MNT = [
    (1, "INCR", 1),
    (2, "SUM", 5)
]

# MDT: (Index, Instruction)
MDT = [
    (1, "INCR &ARG"),
    (2, "MOVER AREG, #1"),
    (3, "ADD BREG, ='1'"),
    (4, "MEND"),
    (5, "SUM &A,&B"),
    (6, "ADD AREG, #1"),
    (7, "ADD BREG, #2"),
    (8, "MEND")
]

# Intermediate code from Pass-1
intermediate = [
    "START 100",
    "INCR A",
    "SUM A,B",
    "END"
]

def line():
    print("-" * 50)

# PASS 2
expanded_code = []

for stmt in intermediate:

    parts = stmt.split()
    name = parts[0]

    # Check if macro call
    found = False

    for m in MNT:
        if m[1] == name:
            found = True

            mdt_ptr = m[2]  # starting index in MDT

            # Get actual arguments
            actual_args = []
            if len(parts) > 1:
                actual_args = parts[1].split(',')

            # Expand macro
            i = mdt_ptr

            while MDT[i-1][1] != "MEND":

                line_mdt = MDT[i-1][1]

                # Replace #1, #2 with actual arguments
                for index, arg in enumerate(actual_args):
                    line_mdt = line_mdt.replace(f"#{index+1}", arg)

                # Skip header line
                if i != mdt_ptr:
                    expanded_code.append(line_mdt)

                i += 1

            break

    # If not macro → keep as it is
    if not found:
        expanded_code.append(stmt)


# OUTPUT
print("\n===== PASS-2 OF TWO PASS MACRO PROCESSOR =====")

print("\nINTERMEDIATE CODE:")
line()
for s in intermediate:
    print(s)

print("\nEXPANDED SOURCE CODE:")
line()
for s in expanded_code:
    print(s)
