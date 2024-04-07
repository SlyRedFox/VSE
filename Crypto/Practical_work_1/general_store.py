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


def checking_input_word(symbols: str) -> bool:
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


def get_check_alpha_key(n_mod_arg: int) -> int:
    """Вввод и проверка ключа alpha"""
    checking_flag: bool = True
    while checking_flag:
        try:
            alpha = int(input(f'Введите ключ alpha.\nТолько взаимно простые элементы с числом {n_mod_arg}: '))
        except Exception as err:
            print(f'Не удалось привести к int введённые данные, это число? Сообщение: {err}')
            simple_exit()

        print('Проверяем введённый ключ alpha...')
        if is_vzaimno_prostoe(n_mod_arg, alpha) == 1:
            checking_flag = False
            print(f'Числа {n_mod_arg} и {alpha} взаимно простые.')
        else:
            print(f'Числа {n_mod_arg} и {alpha} НЕ взаимно простые, введите иной ключ alpha!')
            continue
    return alpha


def get_check_beta_key() -> int:
    """Вввод и проверка ключа beta"""
    check_flag: bool = True
    while check_flag:
        beta = input('Введите ключ beta, для русского алфавита это число от 0 до 32: ')
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
    """Зашифровываем вводное слово, Аффинный шифр"""
    # прописываем соответствие "буква алфавита - номер"
    # перевод элементов слова для шифрования в арабские цифры
    numbers_of_letters: list = []
    for letter in original_word.lower():
        numbers_of_letters.append(rus_lettet_digit[letter])

    # TODO: del
    print(f'numbers_of_letters {numbers_of_letters}')

    # находим список y-ов по ф-ле из раздела "Зашифрование" уi = (alpha * xi + beta) mod n_mod
    # # В базовом случае: x1 = (7 * 2 + 14) % 33
    crypto_symbols: list = list()
    for digit in numbers_of_letters:
        temp_y = (alpha_arg * digit + beta_arg) % n_mod_arg
        crypto_symbols.append(rus_digit_letter[temp_y])
    # TODO: del
    print(f'crypto_symbols {crypto_symbols}')
    return crypto_symbols


def uncrypt_func(original_crypted_word: str, alpha_arg: int, beta_arg: int, n_mod_arg: int) -> list:
    """Расшифровываем изначально зашифрованные данные, Аффинный шифр"""
    # Проверяем элементы зашифрованной фразы по ф-ле из раздела "Расшифрование" xi = alpha**-1 * (yi - beta) mod n_mod
    # с помощью Расширенного алгоритма Евклида найдём обратный элемент
    reverse_element: int = rae(alpha_arg, n_mod_arg)
    # TODO: del
    print(f'reverse_element_RAE {reverse_element}')

    # находим цифры букв
    elements_check: list = list()
    for elem in original_crypted_word:
        temp_x = reverse_element * (rus_lettet_digit[elem] - beta_arg) % n_mod_arg
        elements_check.append(temp_x)
    # TODO: del
    print(f'elements_check_digits_of_letters {elements_check}')

    # восстанавливаем слово
    uncrypted_list: list = list()
    for elem in elements_check:
        temp_letter = rus_digit_letter[elem]
        uncrypted_list.append(temp_letter)
    # TODO: del
    print(f'uncrypted_list_ressurected_word {uncrypted_list}')
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


# Зашифровываем
def crypt_afina_recurr(n_mod_arg: int, our_word_arg: str, alpha_list_arg: list, beta_list_arg: list, alpha_first_key_arg: int, alpha_second_key_arg: int, beta_first_key_arg: int, beta_second_key_arg: int) -> list:
    """Зашифровываем слово/фразу Аффинным рекуррентным шифром"""
    # перевод элементов слова для шифрования в арабские цифры
    numbers_of_letters: list = []
    for letter in our_word_arg.lower():
        numbers_of_letters.append(rus_lettet_digit[letter])

    # TODO: del
    print(f'numbers_of_letters {numbers_of_letters}')

    # Находим список y-ов по ф-ле из раздела "Зашифрование":
    # сохраняем все y-ки в список
    yks_list: list = list()

    # Формула для у1:
    # у1 = (alpha_first_key * x1 + beta_first_key) mod n_mod
    crypto_symbols: list = list()
    y1 = (alpha_first_key_arg * numbers_of_letters[0] + beta_first_key_arg) % n_mod_arg
    crypto_symbols.append(rus_digit_letter[y1])
    yks_list.append(y1)

    # Формула для y2:
    # y2 = (alpha_second_key * x2 + beta_second_key) mod n_mod
    y2 = (alpha_second_key_arg * numbers_of_letters[1] + beta_second_key_arg) % n_mod_arg
    crypto_symbols.append(rus_digit_letter[y2])
    yks_list.append(y2)

    # Формула для последующих yi: произведение двух предыдущих alpha и сумма двух предыдущих beta (оба по n_mod)
    # уi = ((((alpha_first_key * alpha_second_key) mod n_mod) * x3) + ((beta_first_key + beta_second_key) mod n_mod)) mod n_mod
    # берём наш список с третьего элемента (т. к. первые два были для y1 и y2)
    for digit in numbers_of_letters[2:]:
        alpha_next = (alpha_first_key_arg * alpha_second_key_arg) % n_mod_arg
        # добавляем значение в список альф
        alpha_list_arg.append(alpha_next)

        beta_next = (beta_first_key_arg + beta_second_key_arg) % n_mod_arg
        # добавляем значение в список бет
        beta_list_arg.append(beta_next)

        yi = (alpha_next * digit + beta_next) % n_mod_arg
        crypto_symbols.append(rus_digit_letter[yi])
        yks_list.append(yi)

        # создаём новые значения alpha и beta для текущего цикла на основе предыдущих значений
        alpha_first_key_arg = alpha_second_key_arg
        alpha_second_key_arg = alpha_next

        beta_first_key_arg = beta_second_key_arg
        beta_second_key_arg = beta_next

    # TODO: del
    print(f'yks_list {yks_list}')

    # TODO: del
    print(f'crypto_symbols {crypto_symbols}')
    return crypto_symbols


# Расшифровка
def uncrypt_afina_recurr(n_mod_arg: int, our_word_arg: str, alpha_list_arg: list, beta_list_arg: list, alpha_first_key_arg: int, alpha_second_key_arg: int, beta_first_key_arg: int, beta_second_key_arg: int) -> list:
    """Расшифровка полученного значения Аффинного рекуррентного шифра"""
    # сохраняем все y-ки в список: это номера наших зашифрованных букв
    yks_list: list = list()
    # перевод элементов слова для шифрования в арабские цифры
    for letter in our_word_arg.lower():
        yks_list.append(rus_lettet_digit[letter])

    # TODO: del
    print(f'yks_list {yks_list}')

    # находим ключи альфа и бета для расшифровки: начинаем с 3 элемента списка (любого), т. к. по два ключа уже есть
    for x in yks_list[2:]:
        alpha_next = (alpha_first_key_arg * alpha_second_key_arg) % n_mod_arg
        # добавляем значение в список альф
        alpha_list_arg.append(alpha_next)

        beta_next = (beta_first_key_arg + beta_second_key_arg) % n_mod_arg
        # добавляем значение в список бет
        beta_list_arg.append(beta_next)

        # создаём новые значения alpha и beta для текущего цикла на основе предыдущих значений
        alpha_first_key_arg = alpha_second_key_arg
        alpha_second_key_arg = alpha_next

        beta_first_key_arg = beta_second_key_arg
        beta_second_key_arg = beta_next

    # TODO: del
    print(f'alpha_list_arg {alpha_list_arg}')

    # TODO: del
    print(f'beta_list_arg {beta_list_arg}')


    # С помощью Расширенного алгоритма Евклида находим обратный элемент для каждой alpha.
    # Расшифровываем по формуле: alpha_i**-1 * (y_i - beta_i) mod mod_n
    reverse_elements_list: list = list()
    for element in alpha_list_arg:
        reverse_element: int = rae(element, n_mod_arg)
        reverse_elements_list.append(reverse_element)

    # TODO: del
    print(f'reverse_elements_list_rae_for_alpha {reverse_elements_list}')

    decrypt_list: list = list()
    for x in range(len(alpha_list_arg)):
        decrypt_letter = reverse_elements_list[x] * (yks_list[x] - beta_list_arg[x]) % n_mod_arg
        decrypt_list.append(rus_digit_letter[decrypt_letter])

    # TODO: del
    print(f'decrypt_list {decrypt_list}')
    return decrypt_list


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
