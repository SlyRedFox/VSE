# Хранилище
from time import sleep
from random import randrange


# def elliptic_points(a_el: int, b_el: int, x_range_el: tuple) -> list:
#     """Точки на эллиптической кривой y^2 = x^3 + ax + b в диапазоне значений x."""
#     points_list: list = []
#     # Перебираем значения x
#     for x in range(x_range_el[0], x_range_el[1] + 1):
#         y2 = x**3 + a_el * x + b_el
#         if y2 >= 0:  # Проверяем, что y^2 неотрицательно, так как нет действительных корней для отрицательных чисел
#             # Находим целую часть квадратного корня из y^2
#             y = int(y2 ** 0.5)
#
#
#             # Проверяем, что квадрат целого числа равен y^2
#             if y * y == y2:
#                 points_list.append((x, y))
#             if (-y) * (-y) == y2 and y != 0:
#                 points_list.append((x, -y))
#     return points_list


def is_simple_number(number: int, k=10):
    """"Проверка, является ли число простым"""
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0:
        return False

    # малая теорема Ферма
    for iteration in range(k):
        result = randrange(2, number - 1)
        if pow(result, number - 1, number) != 1:
            return False
    return True


def find_simple_q(m: int) -> int:
    """Находит простое число q, удовлетворяющее уравнению: m = n * q"""
    for n in range(1, m + 1):
        # n должно быть делителем m
        if m % n == 0:
            q = m // n
            if is_simple_number(q):
                return q
    # если не удалось найти простое число q, возвращается False
    return False


def simple_exit():
    """Выход из программы"""
    print('\nВведены некорректные данные!\nПерезаапустите программу и выполните корректный ввод!')
    sleep(2)
    exit()


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
