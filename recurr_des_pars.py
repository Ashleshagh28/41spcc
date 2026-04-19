input_string = input("Enter any word: ")
ip = 0


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.middle = None
        self.right = None


def print_tree(root):
    print(f"\n           {root.val}")
    print("        /  |  \\")

    l = root.left.val if root.left else "_"
    m = root.middle.val if root.middle else "_"
    r = root.right.val if root.right else "_"

    print(f"       {l}   {m}   {r}")

    if root.middle:
        ml = root.middle.left.val if root.middle.left else "_"
        mr = root.middle.right.val if root.middle.right else "_"

        if root.middle.left or root.middle.right:
            print("           / \\")
            print(f"          {ml}   {mr}")


def show(title, root):
    print("\n" + title)
    print_tree(root)


def match(ch):
    global ip

    if ip < len(input_string) and input_string[ip] == ch:
        ip += 1
        return True

    return False


def parse():
    global ip

    root = Node("S")
    root.left = Node("_")
    root.middle = Node("X")
    root.right = Node("_")

    root.middle.left = Node("_")
    root.middle.right = Node("_")

    show("Initial Parse Tree Skeleton", root)

    n = len(input_string)

    if n >= 1:
        if match(input_string[0]):
            root.left.val = input_string[0]
            show(f"After matching {input_string[0]}", root)

    if n == 2:
        if match(input_string[1]):
            root.right.val = input_string[1]

    elif n == 3:
        if match(input_string[1]):
            root.middle.left.val = input_string[1]

        if match(input_string[2]):
            root.right.val = input_string[2]

    elif n == 4:
        if match(input_string[1]):
            root.middle.left.val = input_string[1]

        if match(input_string[2]):
            root.middle.right.val = input_string[2]

        if match(input_string[3]):
            root.right.val = input_string[3]

    elif n >= 5:
        if match(input_string[1]):
            root.middle.left.val = input_string[1]

        middle_part = input_string[2:n-1]
        root.middle.val = middle_part

        if match(input_string[2]):
            pass

        ip = n - 1

        if match(input_string[n - 1]):
            root.right.val = input_string[n - 1]

    show("After Expanding Tree", root)

    return root


tree = parse()

if ip == len(input_string):
    show("FINAL PARSE TREE", tree)
else:
    print("Parsing Failed")