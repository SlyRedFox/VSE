# Аффинный рекуррентный шифр
# Базовое слово: вфеврале
from general_store import arabian_digits
from general_store import checkin_input_word
from general_store import true_alphabet
from general_store import simple_exit
from general_store import rae


# словарь {буква: цифра}
rus_lettet_digit: dict = dict(zip(true_alphabet, arabian_digits))
# словарь {цифра: буква}
rus_digit_letter: dict = dict(zip(arabian_digits, true_alphabet))

print('TEST')
print(rus_digit_letter)

# длина русского алфавита, из этой длины random можно выбрать beta
n_mod: int = 33

# нам понадобятся дополнительные ключи
alpha_first: int = 7 # взаимно простое с n_mod
beta_first: int = 14 # random число от 0 до 32, нашего n_mod
alpha_second: int = 5 # взаимно простое с n_mod
beta_second: int = 9 # random число от 0 до 32, нашего n_mod

# списки всех alpha и beta для последующей расшифровки, пока там только по два элемента
alpha_list: list = list()
alpha_list.append(alpha_first)
alpha_list.append(alpha_second)

beta_list: list = list()
beta_list.append(beta_first)
beta_list.append(beta_second)


our_word: str = input('\nЗдравствуй, %username%! \nПожалуйста, введи слово для «Аффинного рекуррентныого шифра» '
                      '(только кириллица). Спасибо! \nP.S.: есть базовая проверка ввода: ')

checkin_input_word(our_word)

# Зашифровываем
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
# у1 = (alpha_first * x1 + beta_first) mod n_mod
crypto_symbols: list = list()
y1 = (alpha_first * numbers_of_letters[0] + beta_first) % n_mod
crypto_symbols.append(rus_digit_letter[y1])
yks_list.append(y1)

# Формула для y2:
# y2 = (alpha_second * x2 + beta_second) mod n_mod
y2 = (alpha_second * numbers_of_letters[1] + beta_second) % n_mod
crypto_symbols.append(rus_digit_letter[y2])
yks_list.append(y2)

# Формула для последующих yi: произведение двух предыдущих alpha и сумма двух предыдущих beta (оба по n_mod)
# уi = ((((alpha_first * alpha_second) mod n_mod) * x3) + ((beta_first + beta_second) mod n_mod)) mod n_mod
# берём наш список с третьего элемента (т. к. первые два были для y1 и y2)
# TODO: del
num = 1
for digit in numbers_of_letters[2:]:
    alpha_next = (alpha_first * alpha_second) % n_mod
    # добавляем значение в спсок альф
    alpha_list.append(alpha_next)

    beta_next = (beta_first + beta_second) % n_mod
    # добавляем значение в спсок бет
    beta_list.append(beta_next)

    # TODO: del
    print(f'\nTEST {num}')
    print(f'alpha_next: {alpha_next}')
    print(f'beta_next: {beta_next}')

    yi = (alpha_next * digit + beta_next) % n_mod
    crypto_symbols.append(rus_digit_letter[yi])
    yks_list.append(yi)

    # TODO: del
    print(f'digit: {digit}')
    print(f'yi: {yi}')

    # создаём новые значения alpha и beta для текущего цикла на основе предыдущих значений
    alpha_first = alpha_second
    alpha_second = alpha_next

    beta_first = beta_second
    beta_second = beta_next

    # TODO: del
    num += 1

print('\nЗашифрованная фраза:')
print(crypto_symbols)


# Расшифровка
print('\n\nРасшифровка. С помощью Расширенного алгоритма Евклида находим обратный элемент для каждой alpha. Затем '
      'расшифровываем по формуле: alpha_i**-1 * (y_i - beta_i) mod mod_n')
reverse_elements_list: list = list()
for element in alpha_list:
    reverse_element: int = rae(element, n_mod)
    reverse_elements_list.append(reverse_element)
    # TODO: del
    # print(f'Результат вычисления РАЕ: {reverse_element}')



# TODO: del
print(f'\nalpha_list {alpha_list}')
print(f'beta_list {beta_list}')
print(f'yks_list {yks_list}')
print(f'reverse_elements_list {reverse_elements_list}')

# Формула расшифровки:
# alpha_i**-1(reverse_elements) * (y_i - beta_i) mod mod_n
# для первых двух
# 19 * (28 - 14) % 33
# 2 -> в
# 20 * (15 - 9) % 33
# 21 -> ф

decrypt_letter: str = ''
for x in range(len(alpha_list)):
    decrypt_letter = reverse_elements_list[x] * (yks_list[x] - beta_list[x]) % n_mod
    # print(decrypt_letter)
    print(rus_digit_letter[decrypt_letter])




# print('\nПроверяем корректность найденного обратного элемента.')
# # Ф-ла: (alpha_first * alpha_first**-1) ≡ 1 * mod n_mod
# # В базовом случае: 7 * 19 ≡ 1 * mod 33 = 133 ≡ 1 * mod 33 = 133 mod 33 = 1
# checking_reverse_element: int = (alpha_first * reverse_element) % n_mod
# if checking_reverse_element == 1:
#     print('Проверка пройдена успешно!')
# else:
#     print('Проверка не пройдена! Завершаем программу...')
#     simple_exit()
#
# # Проверяем по ф-ле из раздела "Расшифрование" xi = alpha**-1 * (yi - beta) mod n_mod
# print('\nПроверяем элементы зашифрованной фразы.')
# elements_check: list = list()
# for elem in crypto_symbols:
#     temp_x = reverse_element * (rus_lettet_digit[elem] - beta_first) % n_mod
#     elements_check.append(temp_x)
#
# print(elements_check)
#
# # Финал-проверка
# final_check: list = list()
# print('\nВосстанавливаем исходное слово-фразу:')
# for elem in elements_check:
#     final_check.append(rus_digit_letter[elem])
#
# our_first_word: str = ''
# for elem in final_check:
#     our_first_word += elem
#
# print(our_first_word)
# if our_first_word == our_word:
#     print('Исходное слово-фраза и расшифровоанное совпадают!')
# else:
#     print('Расшифрованная слово-фраза не совпадает с исходной!')
