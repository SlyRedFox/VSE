# Сравнение первой степени с одним неизвестным

# Здесь сначала используется просто АЕ (Алгоритм Евклида)
# Изначальный пример: 111x ≡ 75 (mod 321) по формуле: ax ≡ b (mod n)

# Вносим a & b для таблицы расчёта АЕ, к формуле они отношения не имеют (a - наибольшее, b - наименьшее)
a: int = 1536
b: int = 102
# а сюда уже вносим данные как из формулы: ax ≡ b (mod n)
a_from_formula: int = 102
b_from_formula: int = 96
n_from_formula: int = 1536
# ВНИМАНИЕ! Если у нас именно задача по сравнению первой степени с одни неизвестным, то нужно внести ниже значение
# переменной ã_base (строка 73)


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

    ã = a_from_formula // a
    b̃ = b_from_formula // a
    ñ = n_from_formula // a

    print(f'\nНаш результат по этой формуле: {ã}*x ≡ {b}*(mod {ñ})')
    print(f'ã = {ã}*x')
    print(f'b̃ = {b̃}')
    print(f'ñ = {ñ}')
    print('Осталось найти ã')

    print(f'\nНаши {a} решения(ий): ')
    print('ã**-1 * b̃')
    for num in range(1, a):
        print(f'ã**-1 * b̃ + ñ * {num}')

    print(f'\nМы нашли b̃, ñ. Нужно найти обратный элемент к ã**-1. В нашем случае нужно найти обратный элемент к {a_from_formula // a}**-1 по модулю {n_from_formula // a}')
    print(f'Это: {a_from_formula // a}**-1 mod {n_from_formula // a} = ?')
    print('Подставляем данные в скрипт 4_rae.py (большее - a, меньшее - b). В результирующую таблицу записываем вместо a - ñ, вместо b - b̃')
    print(f'Если после вычислений обратный элемент к a**-1 получится отрицательный, то для дальнейших расчётов его ОБЯЗАТЕЛЬНО нужно привести по модулю, чтобы сделать положительным: -result mod {n_from_formula // a}')

    print('ВПИШИТЕ РЕЗУЛЬТАТ работы скрипта 4_rae.py для ã в переменную ниже ã_base для дальнейших вычислений. (для примера 111x ≡ 75 (mod 321) будет -26 или 81, если приводим по модулю)')
    ã_base = 81
    print(f'\nМы нашли ã, теперь подставляем все данные в числовом выражении в наши {a} решения(ий).')

    print('Ответ 1')
    print(f'{ã_base} * {b̃} % {ñ} = {ã_base * b̃ % ñ} mod {n_from_formula}')

    for num in range(1, a):
        print(f'Ответ {num + 1}')
        print(f'({ã_base} * {b̃} + {ñ} * {num}) % {n_from_formula} = {(ã_base * b̃ + ñ * num) % n_from_formula}')

    print('\nПроверяем и выписываем все полученные ответы, подставляем их в исходное сравнение. В нашем базовом случае было: 111x ≡ 75 (mod 321)')
    print('Т.е. 111 * 99 ≡ 75 (mod 321) = 10989 mod 321 = 75 (детали в конспектах, страница 32)')

else:
    print('Some strange result.')
