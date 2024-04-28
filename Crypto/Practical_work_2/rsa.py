# Генерация ключей, простые числа p и q, причём p - q = большое число.
# Простое число - это натуральное число > 1, которое делится без остатка на 1 и на себя.
# Шаг 1

def is_simple_number(number: int) -> bool:
    """Проверка, является ли число простым"""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


# key_p: int = int(input('Введите ключ p, условие: это должно быть простое число: '))
# if is_simple_number(key_p):
#     print(f'{key_p} - простое число')
# else:
#     print(f'{key_p} - НЕ простое число')
#     exit()
#
# key_q: int = int(input('Введите ключ q, условие: это должно быть простое число: '))
# if is_simple_number(key_q):
#     print(f'{key_q} - простое число')
# else:
#     print(f'{key_q} - НЕ простое число')
#     exit()

# TODO: del, раскомменить то, что выше
key_p = 109
key_q = 71


# Шаг 2, вычисляем n = p * q (он же открытый ключ)
n: int = key_p * key_q
print(f'Вычисляем n: {n}')

# Шаг 3, вычисляем значение ф-ии Эйлера для n, по ф-ле: f(n) = (p - 1) * (q - 1)
ayler_function_result: int = (key_p - 1) * (key_q - 1)
print(f'Вычисляем значение функции Эйлера f(n): {ayler_function_result}')


# Шаг 4, выбираем экспоненту зашифрования - это целое число e, взаимно простое со значением f(n)
def is_vzaimno_prostoe(number_1: int, number_2: int) -> int:
    """Проверяем, являются ли числа взаимно простыми"""
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1


def get_check_e() -> int:
    """Вввод и проверка числа e"""
    checking_flag: bool = True
    while checking_flag:
        try:
            e_number = int(input(f'\nВведите число e.\nТолько взаимно простое с числом {ayler_function_result}: '))
        except Exception as err:
            print(f'Не удалось привести к int введённые данные, это число? Сообщение: {err}')
            exit()

        print('Проверяем число e.')
        if is_vzaimno_prostoe(ayler_function_result, e_number) == 1:
            checking_flag = False
            print(f'Числа {ayler_function_result} и {e_number} взаимно простые.')
        else:
            print(f'Числа {ayler_function_result} и {e_number} НЕ взаимно простые, введите иное число e!')
            continue
    return e_number


number_e: int = get_check_e()
print(f'Результат, число e: {number_e}')


# Шаг 5, находим экспоненту расшифрования - это целое число d, удовлетворяющее соотношению: e * d ≡ 1(mod f(n)
# TODO: del, в нашем случае это: d = e**-1 mod f(n), d = 13**-1 mod 7560


def rae(e: int, mod_n: int) -> int:
    """Расширенный алгоритм Евклида (на основе файла 4_rae.py), возвращаем обратные элемент. Всегда положительный."""
    a = a_final = mod_n
    b = e

    # default
    x2: int = 1
    x1: int = 0
    y2: int = 0
    y1: int = 1

    def qrxy(a: int, b: int) -> tuple:
        q: int = a // b
        r: int = a % b
        x: int = x2 - q * x1
        y: int = y2 - q * y1
        return q, r, x, y

    # run
    q, r, x, y = qrxy(a, b)

    count: int = 1
    while b != 0:
        q, r, x, y = qrxy(a, b)

        if r == 0:
            d = b
            x = x1
            y = y1
            break

        a: int = b
        b: int = r
        x2: int = x1
        x1: int = x
        y2: int = y1
        y1: int = y
        count += 1

    if y < 0:
        y = y % a_final
    elif y > 0:
        pass
    else:
        print('Иной результат')

    return y


d = close_key = rae(number_e, ayler_function_result)
print(f'Результат, число d (закрытый ключ): {d}')


# Шаг 6, у нас есть пара e, n - это открытый ключ, d - закрытый ключ
open_key: list = [number_e, ayler_function_result]
print(f'Итог по ключам. Открытый ключ: {open_key}. Закрытый ключ: {close_key}')
