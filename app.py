from calculator import add, sub, mul, div
def run():
    print("1) Add\n2) Subtract\n3) Multiply\n4) Divide\n0) Exit")
    choice = input("Select: ")

    if choice == "2": print(("sub(a, b)"))
    a = float(input("a: "))
    b = float(input("b: "))
    if choice == "4": print(div(a, b))
