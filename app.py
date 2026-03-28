"""Simple calculator app."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main():
    print("Calculator v1.0")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 1 = {subtract(5, 1)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"6 / 2 = {divide(6, 2)}")


if __name__ == "__main__":
    main()
