# Аффинный рекуррентный шифр
# Базовое слово: вфеврале, значения ключей: альфа1 = 7, альфа2 = 5; бета1 = 14, бета2 = 9
from general_store import arabian_digits
from general_store import checkin_input_word
from general_store import true_alphabet
from general_store import get_check_beta_key
from general_store import get_check_alpha_key
from general_store import rae
from general_store import simple_exit


# словарь {буква: цифра}
rus_lettet_digit: dict = dict(zip(true_alphabet, arabian_digits))
# словарь {цифра: буква}
rus_digit_letter: dict = dict(zip(arabian_digits, true_alphabet))

# длина русского алфавита, из этой длины random можно выбрать beta
n_mod: int = 33

our_word: str = input('\nЗдравствуйте, %username%! \nПожалуйста, введите слово (или несколько без пробелов) для'
                      ' «Аффинного рекуррентныого шифра» (только кириллица). Спасибо! \nP.S.: есть проверка ввода: ')

# проверка введённых данных
checkin_input_word(our_word)

# TODO: del
# получаем по два ключа alpha и beta
# alpha_first_key: int = 7 # взаимно простое с n_mod
# alpha_second_key: int = 5 # взаимно простое с n_mod
# beta_first_key: int = 14 # random число от 0 до 32, нашего n_mod
# beta_second_key: int = 9 # random число от 0 до 32, нашего n_mod

print('\nВвод и проверка ПЕРВОГО ключа alpha.')
alpha_first_key: int = get_check_alpha_key(n_mod)
print('\nВвод и проверка ВТОРОГО ключа alpha.')
alpha_second_key: int = get_check_alpha_key(n_mod)

print('\nВвод и проверка ПЕРВОГО ключа beta.')
beta_first_key: int = get_check_beta_key()
print('\nВвод и проверка ВТОРОГО ключа beta.')
beta_second_key: int = get_check_beta_key()


# создаём списки всех alpha и beta для последующей расшифровки
alpha_list: list = list()
alpha_list.append(alpha_first_key)
alpha_list.append(alpha_second_key)

beta_list: list = list()
beta_list.append(beta_first_key)
beta_list.append(beta_second_key)


# Зашифровываем
def crypt_afina_recurr(n_mod_arg: int, alpha_first_key: int, alpha_second_key: int, beta_first_key: int, beta_second_key: int) -> list:
    """Зашифровываем слово/фразу Аффинным рекуррентным шифром"""
    # прописываем соответствие "буква алфавита - номер"
    print('\nПеревод элементов слова для шифрования в арабские цифры.')
    numbers_of_letters: list = []
    for letter in our_word.lower():
        numbers_of_letters.append(rus_lettet_digit[letter])

    # TODO: del
    print(f'numbers_of_letters {numbers_of_letters}')

    # Находим список y-ов по ф-ле из раздела "Зашифрование":
    # сохраняем все y-ки в список
    yks_list: list = list()

    # Формула для у1:
    # у1 = (alpha_first_key * x1 + beta_first_key) mod n_mod
    crypto_symbols: list = list()
    y1 = (alpha_first_key * numbers_of_letters[0] + beta_first_key) % n_mod_arg
    crypto_symbols.append(rus_digit_letter[y1])
    yks_list.append(y1)

    # Формула для y2:
    # y2 = (alpha_second_key * x2 + beta_second_key) mod n_mod
    y2 = (alpha_second_key * numbers_of_letters[1] + beta_second_key) % n_mod_arg
    crypto_symbols.append(rus_digit_letter[y2])
    yks_list.append(y2)

    # Формула для последующих yi: произведение двух предыдущих alpha и сумма двух предыдущих beta (оба по n_mod)
    # уi = ((((alpha_first_key * alpha_second_key) mod n_mod) * x3) + ((beta_first_key + beta_second_key) mod n_mod)) mod n_mod
    # берём наш список с третьего элемента (т. к. первые два были для y1 и y2)
    # TODO: del
    num = 1
    for digit in numbers_of_letters[2:]:
        alpha_next = (alpha_first_key * alpha_second_key) % n_mod_arg
        # добавляем значение в список альф
        alpha_list.append(alpha_next)

        beta_next = (beta_first_key + beta_second_key) % n_mod_arg
        # добавляем значение в список бет
        beta_list.append(beta_next)

        # TODO: del
        print(f'\nTEST {num}')
        print(f'alpha_next: {alpha_next}')
        print(f'beta_next: {beta_next}')

        yi = (alpha_next * digit + beta_next) % n_mod_arg
        crypto_symbols.append(rus_digit_letter[yi])
        yks_list.append(yi)

        # TODO: del
        print(f'digit: {digit}')
        print(f'yi: {yi}')

        # создаём новые значения alpha и beta для текущего цикла на основе предыдущих значений
        alpha_first_key = alpha_second_key
        alpha_second_key = alpha_next

        beta_first_key = beta_second_key
        beta_second_key = beta_next

        # TODO: del
        num += 1

     # TODO: del
    print(f'\nalpha_list {alpha_list}')
    print(f'yks_list {yks_list}')
    print(f'beta_list {beta_list}')
    # print('\nЗашифрованная фраза:')  # TODO: del ['ы', 'о', 'а', 'т', 'я', 'ф', 'ы', 'в']
    # print(crypto_symbols)
    return crypto_symbols




# Расшифровка
def uncrypt_afina_recurr(n_mod_arg: int, alpha_list_arg: list, beta_list_arg: list, alpha_first_key_arg: int, alpha_second_key_arg: int, beta_first_key_arg: int, beta_second_key_arg: int) -> list:
    """Расшифровка полученного значения Аффинного рекуррентного шифра"""
    # Находим список y-ов по ф-ле из раздела "Зашифрование":
    # сохраняем все y-ки в список: это номера наших зашифрованных букв
    yks_list: list = list()
    print('\nПеревод элементов слова для расшифрования в арабские цифры.')
    for letter in our_word.lower():
        yks_list.append(rus_lettet_digit[letter])

    # находим ключи альфа и бета для расшифровки: начинаем с 3 элемента, т. к. по два ключа у нас уже есть
    for digit in yks_list[2:]:

        # TODO: del
        print('TESTING PYLAT!!!!!!!!!!!!!!!!!!!!!!')
        print(f'alpha_first_key_arg {alpha_first_key_arg}')
        print(f'alpha_second_key_arg {alpha_second_key_arg}')

        alpha_next = (alpha_first_key_arg * alpha_second_key_arg) % n_mod_arg
        # добавляем значение в список альф
        alpha_list.append(alpha_next)

        beta_next = (beta_first_key_arg + beta_second_key_arg) % n_mod_arg
        # добавляем значение в список бет
        beta_list.append(beta_next)




        # alpha_next = (alpha_first_key * alpha_second_key) % n_mod_arg
        # # добавляем значение в список альф
        # alpha_list.append(alpha_next)
        #
        # beta_next = (beta_first_key + beta_second_key) % n_mod_arg
        # # добавляем значение в список бет
        # beta_list.append(beta_next)

        # создаём новые значения alpha и beta для текущего цикла на основе предыдущих значений
        alpha_first_key_arg = alpha_second_key_arg
        alpha_second_key_arg = alpha_next

        beta_first_key_arg = beta_second_key_arg
        beta_second_key_arg = beta_next


    # С помощью Расширенного алгоритма Евклида находим обратный элемент для каждой alpha.
    # Затем расшифровываем по формуле: alpha_i**-1 * (y_i - beta_i) mod mod_n')
    reverse_elements_list: list = list()
    for element in alpha_list_arg:
        reverse_element: int = rae(element, n_mod_arg)
        reverse_elements_list.append(reverse_element)


    # TODO: del
    print(f'\nalpha_list {alpha_list_arg}')
    print(f'reverse_elements_list {reverse_elements_list}')
    print(f'yks_list {yks_list}')
    print(f'beta_list {beta_list_arg}')

    # Формула расшифровки:
    # alpha_i**-1(reverse_elements) * (y_i - beta_i) mod mod_n
    # для первых двух
    # 19 * (28 - 14) % 33
    # 2 -> в
    # 20 * (15 - 9) % 33
    # 21 -> ф
    # 32 * (0 - 14) % 33

    decrypt_list: list = list()
    for x in range(len(alpha_list_arg)):
        decrypt_letter = reverse_elements_list[x] * (yks_list[x] - beta_list_arg[x]) % n_mod_arg
        decrypt_list.append(rus_digit_letter[decrypt_letter])

    return decrypt_list


# выбор для пользователя
input_user: str = input(f'\nЧто необходимо сделать?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
# вызываем функцию тут, а не в выборе пользователя, т. к. нам нужен список y-ков (yks_list_from_func) для расшифровки


if input_user == '1':
    crypto_phrase = crypt_afina_recurr(n_mod, alpha_first_key, alpha_second_key, beta_first_key, beta_second_key)
    print(crypto_phrase)
    print('\nЗашифрованная фраза/слово: ')
    print(''.join(crypto_phrase))
elif input_user == '2':
    # pass
    uncrypted_word: list = uncrypt_afina_recurr(n_mod, alpha_list, beta_list, alpha_first_key, alpha_second_key, beta_first_key, beta_second_key)
    print('\nРасшифрованная фраза/слово: ')
    print(''.join(uncrypted_word))
else:
    simple_exit()

# 7  5  14  9
# TODO: del  вфеврале   ыоатяфыв
# хиатяфыв платяфыв  йъатяфыв дгатяфыв юоатяфыв шиатяфыв тлатяфыв  мъатяфыв  жгатяфыв боатяфыв  ыиатяфыв

# https://www.bibliofond.ru/view.aspx?id=897442







# # Расшифровка
# print('\n\nРасшифровка. С помощью Расширенного алгоритма Евклида находим обратный элемент для каждой alpha. Затем '
#       'расшифровываем по формуле: alpha_i**-1 * (y_i - beta_i) mod mod_n')
# reverse_elements_list: list = list()
# for element in alpha_list:
#     reverse_element: int = rae(element, n_mod)
#     reverse_elements_list.append(reverse_element)
#     # TODO: del
#     # print(f'Результат вычисления РАЕ: {reverse_element}')
#
#
#
# # TODO: del
# print(f'\nalpha_list {alpha_list}')
# print(f'beta_list {beta_list}')
# print(f'yks_list {yks_list_from_func}')
# print(f'reverse_elements_list {reverse_elements_list}')
#
# # Формула расшифровки:
# # alpha_i**-1(reverse_elements) * (y_i - beta_i) mod mod_n
# # для первых двух
# # 19 * (28 - 14) % 33
# # 2 -> в
# # 20 * (15 - 9) % 33
# # 21 -> ф
#
# decrypt_letter: str = ''
# for x in range(len(alpha_list)):
#     decrypt_letter = reverse_elements_list[x] * (yks_list_from_func[x] - beta_list[x]) % n_mod
#     # print(decrypt_letter)
#     print(rus_digit_letter[decrypt_letter])

