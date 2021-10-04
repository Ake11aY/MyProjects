a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
D = b**2 - 4 * a * c
if D > 0:
    x1 = (-b+(D ** 0.5)) / (2 * a)
    x2 = (-b - (D ** 0.5)) / (2 * a)
    print(x1)
    print(x2)
elif D == 0:
    x = (-b+D) / (2 * a)
    print(x)
else:
    print("D<0")