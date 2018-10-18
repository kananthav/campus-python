import math

def main():
    a, b, c = eval(input("input :"))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2 * a)
    root2 = (-b - discRoot) / (2 * a)

    print("root1:", root1, "root2:", b)

main()
