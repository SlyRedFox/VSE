
# Примечания!
# 1. Для списка binary_numbers  нужно будет внести значения в соответствии с количеством битов, на которые его делим,
# в рассмотренном примере данные делятся в соответствии со значением 11 бит

# 1. Пользователь A задает параметры домена p и g.
# 2. Пользователь A выбирает случайное число x в интервале 1<x<p-1.
print('Параметры домена. Большое простое число p и число G принадлежащее множеству F ')
p = 1283
print(f'p = {p}')

x = 432
print(f'Закрытый ключ 1 < x < p, x = {x}')

g = 3
print(f'g  =  {g}')
poryadok_three = 641
print(f'Порядок тройки из g = {poryadok_three} = 641')

# 3. Пользователь A вычисляет h=g^x  mod⁡p
h = g**x % p
print(f'\nОткрытый ключ h =  {g}**{x} mod {p}, h = {h}')

print('\nАлгоритм формирования подписи *****************************')
print('Шаг 1. Формируем сообщение M ')
M = 'EOO'
print(f'Формируем сообщение M = {M}')


print('\nИнициалы в ASCII:')
ascii_list = [ord(char) for char in M]
print(ascii_list)

print('Переводим в двоичное представление')
bin_ascii: list = []
for key in ascii_list:
      # print(f'{bin(key)[2:]}')
      bin_ascii.append(bin(key)[2:])
print(bin_ascii)

print('Получаем наше M')
M_all_string = ''.join(bin_ascii)
print(M_all_string)

print(f'\nНаходим значение n - размер блока, на который делим. Это log2({p}), результат: n = ')
from math import log2
n: int = int(log2(p))
n = 11 # как в демонстрационной задаче https://my.mts-link.ru/19684723/1008044412/record-new/1775987820 , время 01:10:01
print(n)

print(f'Разделяем на кусочки по {n} битов, сюда вносим наши данные. Нули в начале не нужны')
binary_numbers = ['10', '00010110001', '11010001110']
# Функция для перевода двоичного числа в десятичное
def binary_to_decimal(binary_num):
    return int(binary_num, 2)
# Суммирование десятичных значений двоичных чисел
decimal_sum = sum(binary_to_decimal(num) for num in binary_numbers)

# Перевод обратно в двоичную систему
result_binary = bin(decimal_sum)[2:]
# Перевод в десятичную систему
m = int(result_binary, 2)

print(f'Результат для числа h(M), двоичная, {result_binary}  Десятичная: {m}')

k = 215
print(f'\nШаг 2. Выбираем сеансовый ключ k в интервале 1 < k < p-1. Вычисляем r = g**k mod p, r = {g}**{k} mod {p}')
print(f'k  =  {k}')
r = g**k % p
print(f'r = {r}')

print('\nШаг 3. Вычисляем два числа:u = (m - xr) (mod p - 1) и s = k**-1 * u (mod p-1), где k**=-1 * k   1 (mod p - 1)')
print(f'u = ({m} - {x}*{r}) % ({p} - 1)')
u = (m - x*r) % (p - 1)
print(f'u =  {u}')

print('\nДля вычисления s нам понадобится k**-1, вычисляем его с помощью РАЕ. Если нужно отображение детальных данных, '
      'используй файл 4_rae.py')

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

rae_result = rae(k, p-1)
print(f'Результат работы РАЕ: {rae_result}')
print('Находим по формуле s = k**-1 * u (mod p-1)')
print(f'Исходные данные: s = {rae_result} * {u} (mod {p}-1)')
s = (rae_result * u) % (p-1)
print(f's = {s}')

print(f'\nШаг 4. Пользователь А передаёт В список параметров Электронной Подписи: M = {M}, r = {r}, s = {s}')
