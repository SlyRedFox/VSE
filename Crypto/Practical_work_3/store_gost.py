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