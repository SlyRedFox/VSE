import math

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


# Шаг 2, вычисляем n = p * q
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


# Зашифрование
# Шаг 1, на мнужны именно двоичные представления чисел из ASCII таблицы
def symbol_to_asc2_binary(letter: str) -> str:
    """Преобразование символа в двоичное представление"""
    binary_code = bin(ord(letter))[2:].zfill(8)
    return binary_code


# TODO: del, это будет из файла
code_string: str = 'code'
# выстраиваем строку из символов в двоичном представление
final_binary_code: str = ''.join(symbol_to_asc2_binary(symbol) for symbol in code_string)
# TODO: del, это будет из файла
print(f'\nСообщение в виде бинарного кода: {final_binary_code}')


# Представим сообщение в виде последовательности чисел: m1, m2... mn
# Вычисляем длину блока - именно для Открытого Текста! - по формуле: log2(number)
# Логарифм двоичный n: log2(n) с округлением вниз: math.floor().
# TODO: del, наше число n, которое вычисляли выше
# number = 7739

binary_log: int = math.floor(math.log2(n))
print(f'Длина блока по формуле log2(число) равна: {binary_log}')

# в нашем базовом случае длина блока равна 12 бит, берём их с конца, т.к. начало в случае
# необходимости можно дополнить незначащими нулями, а если добавим их в конец - это уже будет другое значение).
print(f'\nБерём данные бинарного кода {final_binary_code}, считаем с конца {binary_log} бит.')

# нужно узнать длину для цикла, для этого берём длино бинарного лога и делим её на длину блока.
# в базовом случае это будет 2, но нужно добавить +1, т.к. есть ещё "кусочек" блока короче 12, пример:
len_cycle: int = (len(final_binary_code) // binary_log) + 1
# TODO: del, длина для цикла
print(f'\nДлина блока для цикла: {len_cycle}\n')

# для базового примера:
# 01100011011011110110010001100101 - основной блок
# 010001100101 - первый блок
# 011011110110 - второй блок
# 01100011 - третий блок, который нужно дополнять нулями слева
final_binary_code_int = int(final_binary_code, 2)
result_list_binary: list = []
for i in range(len_cycle):
    if len(final_binary_code) > binary_log:
        print('Длина позволяет') # TODO: del
        result_list_binary.append(final_binary_code[(binary_log*-1):])
        final_binary_code = final_binary_code[:(binary_log*-1)]
    else:
        print('Длина не позволяет') # TODO: del ВОЗМОЖНО, ТУТ НУЖНО ДОПОЛНЯТЬ НУЛЯМИ!!!
        print(f'Сейчас имеем значение: {final_binary_code}')
        result_list_binary.append(final_binary_code)

print(f'Результат после цикла в списке: {result_list_binary}')


# # берём значения с конца, поэтому из 12 делаем -12 вот так: [(binary_log*-1):]
# otrezok_example: str = final_binary_code[(binary_log*-1):]
# print(f'Это первый блок m1. "Кусочек" длиной в {binary_log} бит: {otrezok_example}')
#
# m1: int = int(otrezok_example, 2)

print(f'Переводим каждый элемент полученного списка в десятичное представление.')
result_list_dec: list = []
for element in result_list_binary:
    result_list_dec.append(int(element, 2))
print(f'Десятичный вид после цикла в списке: {result_list_dec}')


print('\nЗашифровываем блоки по формуле: Ci = Mi**n (mod n)')
crypted_message: list = list()
for element in result_list_dec:
    crypted_message.append(element**number_e % n)
print(f'Зашифрованное сообщение в десятичном виде: {crypted_message}')

# в ШифроТексте необходимо, чтобы все его блоки имели одинаковую длину: log2(n) + 1
# # в случае необходимости дополняем незначащими нулями слева zfill(binary_log+1
print('Переводим его в двоичный вид.')
crypted_message_bin: list = list()
for element in crypted_message:
    crypted_message_bin.append(bin(element)[2:].zfill(binary_log+1))
print(f'Результат в двоичном представление. Это наш ШифроТекст: {crypted_message_bin}')


# # Расшифровка
print('\nРасшифровка.')
# # Шаг 1, берём бинарную последовательность c1, c2... cn и переводим в десятичное представление
crypted_message_dec: list = list()
for element in crypted_message_bin:
    crypted_message_dec.append(int(element, 2))
print(f'Результат в десятичном виде: {crypted_message_dec}')

# ci_decrypted_dec: int = int(binary_code_ci, 2)
# print(f'Десятичное представление символа: {ci_decrypted_dec}')



# Шаг 2, вычисляем значение символа по формуле: Mi = Ci**d (mod n).
# # В нашем случае: Mi = 3061**6397 (mod n) TODO: del
print('\nВычисляем значение символа по формуле: Mi = Ci**d (mod n).')
uncrypted_message_dec: list = list()
for element in crypted_message_dec:
    uncrypted_message_dec.append(element**d % n)
print(f'Получено десятичное представление символа: {uncrypted_message_dec}')


# ci_symbol_dec: int = c_i**d % n
# print(f'Полученное десятичное представление символа: {ci_symbol_dec}')

print('Переводим в двоичный вид.')
binary_code_uncrypted: list = list()
for element in uncrypted_message_dec:
    binary_code_uncrypted.append(bin(element)[2:].zfill(binary_log))
print(f'Расшифрованное сообщение в двоичном виде: {binary_code_uncrypted}')

# реверсируем полученный список
binary_code_uncrypted_reverse: list = binary_code_uncrypted[::-1]
print(f'Расшифрованное сообщение в двоичном виде: {binary_code_uncrypted_reverse}')


binary_final_string: str = ''.join(binary_code_uncrypted_reverse)
print(f'Получаем строку с зашифрованным сообщением, двоичное представление: {binary_final_string}')

print('Разделяем полученные данные на блоки по 8 бит и находим совпадения в ASCII таблице.')
# в базовом варианте финал-строка выглядит так: 000001100011011011110110010001100101
# если смотреть с конца, то вы чётко выделяем четыре блока по 8 бит, а четыре ноля в начале будут "лишние":
# 0000 01100011 01101111 01100100 01100101
# поэтому мы просто целочисленно делим строку на блоки по 8 бит и сравниваем каждый блок с ASCII таблицей
bit_length: int = 8
len_final_cycle: int = (len(binary_final_string) // bit_length)
final_list: list = list()
for i in range(len_final_cycle):
    final_list.append(binary_final_string[(bit_length * -1):])
    binary_final_string = binary_final_string[:(bit_length * -1)]
final_reverse_list = final_list[::-1]
print(final_reverse_list)

for element in final_reverse_list:
    print(chr(int(element, 2)), end='')
