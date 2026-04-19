def loop_invariant():
    print("\n--- Loop Invariant Code Motion ---")

    print("\nOriginal Code:")
    print("while i < n:")
    print("    x = a + b")
    print("    y = x * i")
    print("    i += 1")

    print("\nOptimized Code:")
    print("x = a + b")
    print("while i < n:")
    print("    y = x * i")
    print("    i += 1")


def strength_reduction():
    print("\n--- Strength Reduction ---")

    print("\nOriginal Code:")
    print("y = x * 2")

    print("\nOptimized Code:")
    print("y = x << 1")


def dead_code_elimination():
    print("\n--- Dead Code Elimination ---")

    print("\nOriginal Code:")
    print("a = 10")
    print("b = 20")
    print("c = a + b")
    print("c = 50")

    print("\nOptimized Code:")
    print("a = 10")
    print("b = 20")
    print("c = 50")


def common_subexpression():
    print("\n--- Common Subexpression Elimination ---")

    print("\nOriginal Code:")
    print("a = b * c + d")
    print("e = b * c + f")

    print("\nOptimized Code:")
    print("t = b * c")
    print("a = t + d")
    print("e = t + f")


def main():
    while True:
        print("\n==== CODE OPTIMIZATION MENU ====")
        print("1. Loop Invariant Code Motion")
        print("2. Strength Reduction")
        print("3. Dead Code Elimination")
        print("4. Common Subexpression Elimination")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            loop_invariant()
        elif choice == '2':
            strength_reduction()
        elif choice == '3':
            dead_code_elimination()
        elif choice == '4':
            common_subexpression()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()