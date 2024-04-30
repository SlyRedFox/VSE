from time import sleep
import math
from random import randrange


# def is_simple_number(number: int) -> bool:
#     """Проверка, является ли число простым"""
#     if number <= 1:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True

def is_simple_number(number: int, k=10):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0:
        return False

    # малая теорем Ферма
    for iteration in range(k):
        result = randrange(2, number - 1)
        if pow(result, number - 1, number) != 1:
            return False
    return True


def is_vzaimno_prostoe(number_1: int, number_2: int) -> int:
    """Проверяем, являются ли числа взаимно простыми"""
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1


def get_check_e(ayler_function: int) -> int:
    """Вввод и проверка числа e"""
    checking_flag: bool = True
    while checking_flag:
        try:
            e_number = int(input(f'\nВведите число e.\nТолько взаимно простое с числом: {ayler_function} \nВаш ввод: '))
        except Exception as err:
            print(f'Не удалось привести к int введённые данные, это число? Сообщение: {err}')
            simple_exit()

        print('Проверяем число e.')
        if is_vzaimno_prostoe(ayler_function, e_number) == 1:
            checking_flag = False
            print(f'Числа {ayler_function} и {e_number} взаимно простые.')
        else:
            print(f'Числа {ayler_function} и {e_number} НЕ взаимно простые, введите иное число e!')
            continue
    return e_number


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


def symbol_to_asc2_binary(letter: str) -> str:
    """Преобразование символа в двоичное представление"""
    binary_code = bin(ord(letter))[2:].zfill(8)
    return binary_code


def encrypt_message(n, message: str, num_e: int) -> list:
    """Зашифровать полученное сообщение"""
    final_binary_code: str = ''.join(symbol_to_asc2_binary(symbol) for symbol in message)
    print(f'\nСообщение в виде бинарного кода: {final_binary_code}')

    # Представим сообщение в виде последовательности чисел: m1, m2... mn
    # Вычисляем длину блока - именно для Открытого Текста! - по формуле: log2(number)
    # Логарифм двоичный n: log2(n) с округлением вниз: math.floor().
    binary_log: int = math.floor(math.log2(n))
    # binary_log: int = 12 TODO: del
    print(f'Длина блока по формуле log2(число) равна: {binary_log}')

    # в нашем базовом случае длина блока равна 12 бит, берём их с конца, т.к. начало в случае
    # необходимости можно дополнить незначащими нулями, а если добавим их в конец - это уже будет другое значение).
    print(f'\nБерём данные бинарного кода {final_binary_code}, считаем с конца {binary_log} бит.')

    # нужно узнать длину для цикла, для этого берём длино бинарного лога и делим её на длину блока.
    # в базовом случае это будет 2, но нужно добавить +1, т.к. есть ещё "кусочек" блока короче 12, пример:
    len_cycle: int = (len(final_binary_code) // binary_log) + 1
    print(f'\nДлина блока для цикла: {len_cycle}\n')

    # для базового примера:
    # 01100011011011110110010001100101 - основной блок
    # 010001100101 - первый блок
    # 011011110110 - второй блок
    # 01100011 - третий блок, который можно дополнять нулями слева
    # берём значения с конца, поэтому из 12 делаем -12 вот так: [(binary_log*-1):]
    final_binary_code_int = int(final_binary_code, 2)
    result_list_binary: list = []
    for i in range(len_cycle):
        if len(final_binary_code) > binary_log:
            result_list_binary.append(final_binary_code[(binary_log * -1):])
            final_binary_code = final_binary_code[:(binary_log * -1)]
        else:
            print(f'Сейчас имеем значение: {final_binary_code}')
            result_list_binary.append(final_binary_code)

    print(f'Результат после цикла в списке: {result_list_binary}')

    print(f'Переводим каждый элемент полученного списка в десятичное представление.')
    result_list_dec: list = []
    for element in result_list_binary:
        result_list_dec.append(int(element, 2))
    print(f'Десятичный вид после цикла в списке: {result_list_dec}')

    print('\nЗашифровываем блоки по формуле: Ci = Mi**n (mod n)')
    crypted_message: list = list()
    for element in result_list_dec:
        crypted_message.append(element ** num_e % n)
    print(f'Зашифрованное сообщение в десятичном виде: {crypted_message}')

    # в ШифроТексте необходимо, чтобы все его блоки имели одинаковую длину: log2(n) + 1
    # # в случае необходимости дополняем незначащими нулями слева zfill(binary_log+1
    # переводим в двоичный вид
    crypted_message_bin: list = list()
    for element in crypted_message:
        crypted_message_bin.append(bin(element)[2:].zfill(binary_log + 1))
    print(f'Результат в двоичном представление, наш ШифроТекст: {crypted_message_bin}')
    return crypted_message_bin


def pow_mod_for_mi(elem, num_d, n):
    """Возведение в степень по модулю, большие числа"""
    result = pow(elem, num_d, n)
    return result


def decrypt_message(n, crypted_message: list, num_d: int) -> None:
    # Расшифровка
    # Шаг 1, берём бинарную последовательность c1, c2... cn и переводим в десятичное представление
    print('\nРасшифровка.')
    crypted_message_dec: list = list()
    for element in crypted_message:
        crypted_message_dec.append(int(element, 2))
    print(f'Результат в десятичном виде: {crypted_message_dec}')

    # Шаг 2, вычисляем значение символа по формуле: Mi = Ci**d (mod n).
    print('\nВычисляем значение символа по формуле: Mi = Ci**d (mod n).')
    uncrypted_message_dec: list = list()
    for element in crypted_message_dec:
        # print(element) TODO: del
        # print(num_d)
        # print(n)
        uncrypted_message_dec.append(pow_mod_for_mi(element, num_d, n))
    print(f'Получено десятичное представление символа: {uncrypted_message_dec}')

    # переводим в двоичный вид
    binary_log: int = math.floor(math.log2(n))
    print(f'Длина блока по формуле log2(число) равна: {binary_log}')

    binary_code_uncrypted: list = list()
    for element in uncrypted_message_dec:
        # binary_code_uncrypted.append(bin(element)[2:])
        binary_code_uncrypted.append(bin(element)[2:].zfill(binary_log)) #TODO: del длина блока только для Открытого Текста

    # реверсируем полученный список
    binary_code_uncrypted_reverse: list = binary_code_uncrypted[::-1]
    print(f'Расшифрованное сообщение в двоичном виде: {binary_code_uncrypted_reverse}')

    binary_final_string: str = ''.join(binary_code_uncrypted_reverse)
    print(f'Получаем строку с зашифрованным сообщением, двоичное представление: {binary_final_string}')

    print('\nРазделяем полученные данные на блоки по 8 бит и находим совпадения в ASCII таблице.')
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
    # переворачиваем список
    final_reverse_list = final_list[::-1]

    # убираем [00000000] в начале данных, т.к. это незначимый символ
    if final_reverse_list[0] == '00000000':
        final_reverse_list.pop(0)
    print(f'Финальные данные для расшифровки в двоичном виде:{final_reverse_list}')

    print('Исходный текст: ')
    for element in final_reverse_list:
        print(chr(int(element, 2)), end='')


def simple_exit():
    """Выход из программы"""
    print('\nВведены некорректные данные!\nПерезаапустите программу и выполните корректный ввод!')
    sleep(2)
    simple_exit()
