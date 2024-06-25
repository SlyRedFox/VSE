import sympy as sp

# Определяем символ x
x = sp.symbols('x')

# Определяем неприводимый многочлен x^3 + 2x^2 + 2x + 2
modulus = sp.Poly(x**3 + 2*x**2 + 2*x + 2, x)

# Определяем элемент 2x^2 + x
element = sp.Poly(2*x**2 + x, x)

# Функция для умножения двух многочленов в поле Галуа
def galua_multiply(a, b, modulus, p):
    product = (a * b).trunc(p)
    return product % modulus

# Функция для нахождения порядка элемента в поле Галуа
def find_order(element, modulus, p=3):
    identity = sp.Poly(1, x)
    power = element
    order = 1
    while power != identity:
        power = galua_multiply(power, element, modulus, p)
        order += 1
        if order > p**3:
            return -1  # Если порядок элемента больше, чем размер поля, возвращаем -1
    return order

# Нахождение порядка элемента
order = find_order(element, modulus)
print("Порядок элемента:", order)