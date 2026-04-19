precedence = {
    '^': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1
}

operators = {'+', '-', '*', '/', '^'}


def infix_to_postfix(expression):
    expression = expression.replace(" ", "")
    expression = expression.replace("–", "-")
    expression = expression.replace("—", "-")

    stack = []
    postfix = []

    for ch in expression:

        if ch.isalnum():
            postfix.append(ch)

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())

            if stack:
                stack.pop()

        elif ch in operators:
            while (stack and stack[-1] != '(' and
                   precedence[ch] <= precedence.get(stack[-1], 0)):
                postfix.append(stack.pop())

            stack.append(ch)

    while stack:
        postfix.append(stack.pop())

    return ''.join(postfix)


def generate_TAC(postfix):
    stack = []
    tac = []
    temp_count = 1

    for ch in postfix:

        if ch.isalnum():
            stack.append(ch)

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            temp = f"t{temp_count}"
            temp_count += 1

            tac.append(f"{temp} = {op1} {ch} {op2}")
            stack.append(temp)

    return tac


def generate_quadruple(tac):
    quadruple = []

    for line in tac:
        left, right = line.split("=")

        result = left.strip()
        op1, operator, op2 = right.strip().split()

        quadruple.append((operator, op1, op2, result))

    return quadruple


def generate_triple(tac):
    triple = []

    for line in tac:
        _, right = line.split("=")

        op1, operator, op2 = right.strip().split()

        triple.append((operator, op1, op2))

    return triple


if __name__ == "__main__":

    expr = input("Enter Infix Expression or Equation: ")

    if '=' in expr:
        lhs, rhs = expr.split('=')

        lhs = lhs.strip()
        rhs = rhs.strip()

        print("\nLHS :", lhs)
        print("RHS :", rhs)

        postfix = infix_to_postfix(rhs)

    else:
        lhs = ""
        postfix = infix_to_postfix(expr)

    print("\nPostfix Expression:", postfix)

    tac = generate_TAC(postfix)

    print("\nThree Address Code:")
    for line in tac:
        print(line)

    if lhs and tac:
        last_temp = tac[-1].split("=")[0].strip()
        print(f"{lhs} = {last_temp}")

    quadruple = generate_quadruple(tac)

    print("\nQuadruple Representation:")
    print("Op\tArg1\tArg2\tResult")

    for q in quadruple:
        print(f"{q[0]}\t{q[1]}\t{q[2]}\t{q[3]}")

    triple = generate_triple(tac)

    print("\nTriple Representation:")
    print("Index\tOp\tArg1\tArg2")

    for i, t in enumerate(triple):
        print(f"{i}\t{t[0]}\t{t[1]}\t{t[2]}")