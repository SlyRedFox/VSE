# Расширенный Алгоритм Евклида
# Находим обратный элемент по модулю

# Внести параметры: a & b (равны), a_final & b_final (равны)
# Параметры для данной задаче: найти обратный элемент к 1721 по модулю 2379
# 1721**-1 mod 2379
a = a_final = 107
b = b_final = 37


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
        d = b
        x = x1
        y = y1
        break

    print(f'\nResult_{count}: q = {q}, r = {r}, x = {x}, y = {y}, a = {b}, b = {r}, x2 = {x1}, x1 = {x}, y2 = {y1}, y1 = {y}')

    a: int = b
    b: int = r
    x2: int = x1
    x1: int = x
    y2: int = y1
    y1: int = y
    count += 1

print(f'\nВычисляем результат-элементы: \nd = {d}, x = {x}, y = {y}')
print(f'Финальный результат по формуле: xa + yb = NOD(a, b) = d --> {x}*{a_final} (starting a) + {y}*{b_final} (starting b) = NOD({a_final}, {b_final}) = 1')
print(f'Финальный ответ, {b_final}**-1 mod {a_final} = {y} (это y, искомый обратный элемент)')

fin_cheking: int = y * b_final % a_final
print(f'Checking: {y} * {b_final} % {a_final} =  {fin_cheking}')

print('\nЕсли результат отрицательное число, это тоже верный ответ. Но если мы хотим использовать его для дальнейших расчётов (расчёт РАЕ - часть задачи), то ОБЯЗАТЕЛЬНО приводим его по модулю, чтобы сделать положительным. \nВ нашем случае:')

if y < 0:
    print(f'- отрицательный результат, можем вычислить по модулю положительный, итог: {y % a_final}')
elif y > 0:
    print('- положительный результат')
else:
    print('Иной результат')
