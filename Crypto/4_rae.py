# base params for task 1721**-1 mod 2379
a: int = 2379
b: int = 1721

# default
x2: int = 1
x1: int = 0
y2: int = 0
y1: int = 1


def qrxy(a: int, b: int) -> tuple:
    q: int = a // b
    r: int = a % b
    x: int = x2 - q*x1
    y: int = y2 - q*y1
    return q, r, x, y


# run
q, r, x, y = qrxy(a, b)
print(f'\nZero_Result: q = -, r = -, x = -, y = -, a = {a}, b = {b}, x2 = {x2}, x1 = {x1}, y2 = {y2}, y1 = {y1}')

count: int = 1
while b != 0:
    q, r, x, y = qrxy(a, b)

    if r == 0:
        print(f'\nResult_{count}: q = {q}, r = {r}, x = -, y = -, a = {b}, b = {r}, x2 = {x1}, x1 = -, y2 = {y1}, y1 = -')
        break

    print(f'\nResult_{count}: q = {q}, r = {r}, x = {x}, y = {y}, a = {b}, b = {r}, x2 = {x1}, x1 = {x}, y2 = {y1}, y1 = {y}')

    a: int = b
    b: int = r
    x2: int = x1
    x1: int = x
    y2: int = y1
    y1: int = y
    count += 1
