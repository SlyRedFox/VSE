# Хранилище переменных
from time import sleep

# Шифр простой замены
true_alphabet: list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                       'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

crypto_alphabet: list = ['с', 'п', 'ф', 'ш', 'ц', 'я', 'э', 'в', 'ъ', 'ы', 'з', 'д', 'х', 'л', 'у', 'ч', 'г', 'ю', 'ь',
                         'б', 'р', 'о', 'е', 'м', 'ё', 'н', 'и', 'щ', 'т', 'к', 'й', 'ж', 'а']

# для проверки корректного ввода, английский алфавит и спецсимволы
eng_alphabet_spec: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'i',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(',
                           ')', '_', '+', '-', '"', '№', ';', ':', '?', '<', '>', ',' '.', '/', '\\', '|', '', '~',
                           '»', '{', '}', '[', ']', '=', '', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A',
                           'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# ф-ия выхода
def simple_exit():
    print('\nВведены некорректные данные!\nПожалуйста, запустите программу заново и выполните корректный ввод!')
    sleep(2)
    exit()


def checkin_input_word(symbols: str) -> bool:
    """Проверка введённых %username% данных"""
    print('\nПроверочная фаза, пожалуйста, подождите...')
    sleep(1)
    if len(symbols) == 0:
        simple_exit()

    for key in symbols:
        print(f'Тщательно проверяем символ: {key}')
        if (len(key) == 0) or (key in eng_alphabet_spec):
            simple_exit()
    print('Проверка пройдена успешно!')
    return True


# Аффинный шифр и Аффинный рекуррентный шифр
arabian_digits: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

# если понадобится английский алфавит
# digits_eng: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
# eng_alphabet: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'i', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# eng_lettet_digit: dict = dict(zip(eng_alphabet, arabian_digits))


# метод поиска делителей, пока в нём нет необходимости, сохранил на всякий случай
# def find_delitels(input_num: int) -> list:
#     """Находим делители для проверки ключей alpha"""
#     temp_div_list: list = list()
#     print(f'Делители числа {input_num}:')
#     for elem in range(1, input_num + 1):
#         if input_num % elem == 0:
#             temp_div_list.append(elem)
#     return temp_div_list


def is_vzaimno_prostoe(n_num, alpha):
    """Проверяем, являются ли числа взаимно простыми"""
    while alpha:
        n_num, alpha = alpha, n_num % alpha
    return n_num


# словарь {буква: цифра}
rus_lettet_digit: dict = dict(zip(true_alphabet, arabian_digits))
# словарь {цифра: буква}
rus_digit_letter: dict = dict(zip(arabian_digits, true_alphabet))


def checking_beta_key() -> int:
    """Вввод и проверка ключа beta"""
    check_flag: bool = True
    while check_flag:
        beta = input('\nВведите ключ beta, для русского алфавита это число от 0 до 32: ')
        try:
            beta = int(beta)
        except Exception as err:
            print(f'Не удалось привести к int введённые данные, это число? Сообщение: {err}')
            simple_exit()

        print('Проверяем введённый ключ...')
        if 0 <= beta <= 32:
            print('Ключ beta корректный!')
            check_flag = False
        else:
            print('Ключ вне указанного диапазона! Введите другой ключ.')
            continue

    return beta


def crypt_func(original_word: str, alpha_arg: int, beta_arg: int, n_mod_arg: int) -> list:
    """Зашифровываем вводное слово"""
    # прописываем соответствие "буква алфавита - номер"
    # перевод элементов слова для шифрования в арабские цифры
    numbers_of_letters: list = []
    for letter in original_word.lower():
        numbers_of_letters.append(rus_lettet_digit[letter])

    # находим список y-ов по ф-ле из раздела "Зашифрование" уi = (alpha * xi + beta) mod n_mod
    # # В базовом случае: x1 = (7 * 2 + 14) % 33
    crypto_symbols: list = list()
    for digit in numbers_of_letters:
        temp_y = (alpha_arg * digit + beta_arg) % n_mod_arg
        crypto_symbols.append(rus_digit_letter[temp_y])
    return crypto_symbols


def uncrypt_func(original_crypted_word: str, alpha_arg: int, beta_arg: int, n_mod_arg: int) -> list:
    """Расшифровываем изначально зашифрованные данные"""
    # Проверяем элементы зашифрованной фразы по ф-ле из раздела "Расшифрование" xi = alpha**-1 * (yi - beta) mod n_mod
    # с помощью Расширенного алгоритма Евклида найдём обратный элемент
    reverse_element: int = rae(alpha_arg, n_mod_arg)

    # находим цифры букв
    elements_check: list = list()
    for elem in original_crypted_word:
        temp_x = reverse_element * (rus_lettet_digit[elem] - beta_arg) % n_mod_arg
        elements_check.append(temp_x)

    # восстанавливаем слово
    uncrypted_list: list = list()
    for elem in elements_check:
        temp_letter = rus_digit_letter[elem]
        uncrypted_list.append(temp_letter)
    return uncrypted_list


# это поиск обратного элемента по РАЕ и его проверка, если понадобится
# def checking_crypto_phrase():
#     """Проверяем найденные элементы"""
#     print('\nОсуществляем проверку. С помощью Расширенного алгоритма Евклида найдём обратный элемент.')
#     reverse_element: int = rae(alpha, n_mod)
#     print(f'Результат вычисления РАЕ: {reverse_element}')
#
#     print('\nПроверяем корректность найденного обратного элемента.')
#     # Ф-ла: (alpha * alpha**-1) ≡ 1 * mod n_mod
#     # В базовом случае: 7 * 19 ≡ 1 * mod 33 = 133 ≡ 1 * mod 33 = 133 mod 33 = 1
#     checking_reverse_element: int = (alpha * reverse_element) % n_mod
#     if checking_reverse_element == 1:
#         print('Проверка пройдена успешно!')
#     else:
#         print('Проверка не пройдена! Завершаем программу...')
#         simple_exit()


def rae(alpha: int, mod_n: int) -> int:
    """Расширенный алгоритм Евклида (на основе файла 4_rae.py), возвращаем обратные элемент. Всегда положительный."""
    a = a_final = mod_n
    b = alpha

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
