# Сравнение первой степени с одним неизвестным

# Здесь сначала используется просто АЕ (Алгоритм Евклида)
# Изначальный пример: 111x ≡ 75 (mod 321) по формуле: ax ≡ b (mod n)

# Вносим a & b для таблицы расчёта АЕ, к формуле они отношения не имеют (a - наибольшее, b - наименьшее)
a: int = 321
b: int = 111

# а сюда уже вносим данные как из формулы: ax ≡ b (mod n)
a_from_formula: int = 111
b_from_formula: int = 75
n_from_formula: int = 321


# начало АЕ
def cycle_change(a: int, b: int) -> tuple:
    r_temp: int = a % b
    a_temp: int = b
    b_temp: int = r_temp
    return r_temp, a_temp, b_temp


count: int = 1
print(f'Zero line: r = -, a = {a}, b = {b}')
while b != 0:
    r_next, a_next, b_next = cycle_change(a, b)

    print(f'Result_{count}: r = {r_next}, a = {a_next}, b = {b_next}')
    a: int = a_next
    b: int = b_next
    count += 1

    if b_next == 0:
        print('b = 0 (!)')

print(f'\nFinal result: a = {a}')
# конец АЕ


if a == 1:
    print('Вариант 1, x = a**-1 * b')
    # TODO check it, not shure...
    print(f'Result: {(a_from_formula**-1) * b_from_formula}')
elif (a > 1) and (b_from_formula % a) > 0:
    print('Вариант 2, d не делит b, решений нет')
elif (a > 1) and (b_from_formula % a) == 0:
    print(f'Вариант 3, d делит b, у нас {a} решения(ий) по модулю n')
    print('Создаём новую форму сравнения по формуле: a/d*x ≡ b/d * mod n/d')
    print(f'Результат: {a_from_formula // a}*x ≡ {b_from_formula // a}*(mod {n_from_formula // a})')

    print(f'Наши {a} решения(ий): ')
    print('ã**-1 * b̃')
    for num in range(1, a):
        print(f'ã**-1 * b̃ + ñ * {num}')

    print(f'\nМы нашли b̃, ñ. Нужно найти обратный элемент к ã**-1. В нашем случае нужно найти обратный элемент к {a_from_formula // a}**-1 по модулю {n_from_formula // a}')
    print(f'Это: {a_from_formula // a}**-1 mod {n_from_formula // a} = ?')
    print('Подставляем данные в скрипт 4_rae.py (большее - a, меньшее - b). В результирующую таблицу записываем вместо a - ñ, вместо b - b̃')
    print(f'Если после вычислений обратный элемент к a**-1 получится отрицательный, то для дальнейших расчётов его лучше привести по модулю, чтобы сделать положительным: -result mod {n_from_formula // a}')

else:
    print('Some strange result.')
