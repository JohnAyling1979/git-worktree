"""Simple calculator app."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    print("Calculator v1.0")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 1 = {subtract(5, 1)}")


if __name__ == "__main__":
    main()
