a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
c = int(input("Nhap vao so c: "))
delta = b**2 - 4*a*c
print(delta)
x1 = (-b + delta**0.5) / (2 * a)
x2 = (-b - delta**0.5) / (2*a)
print(x1)
print(x2)

