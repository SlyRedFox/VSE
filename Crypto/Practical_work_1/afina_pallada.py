# Аффинный шифр
# Шифр подстановочный. Криптографическое преобразование заменяет символы открытого текста на другие по правилу.
# Базовое слово: вфеврале
from pprint import pprint
from general_store import arabian_digits
from general_store import checkin_input_word
from general_store import is_vzaimno_prostoe

from general_store import checking_beta_key
from general_store import true_alphabet
from general_store import simple_exit
from general_store import rae


# длина русского алфавита
n_mod: int = 33

# словарь {буква: цифра}
rus_lettet_digit: dict = dict(zip(true_alphabet, arabian_digits))
# словарь {цифра: буква}
rus_digit_letter: dict = dict(zip(arabian_digits, true_alphabet))


# запрос ввода данных от пользователя
our_word: str = input('\nЗдравствуй, %username%! \nПожалуйста, введи слово для «Аффинного шифра» (только кириллица). '
                      'Спасибо! \nP.S.: есть базовая проверка ввода: ')

# проверка введённых данных
checkin_input_word(our_word)

# alpha может относиться только к группе обратимых элементов кольца класса вычетов.
# Это элементы, которые взаимно простые с числом n_mod, т. е. те, у которых НОД с n_mod = 1
# Пример:
# Число 7 взаимно простое с 33, т.к. у них разные простые множители, и они не имеют общих делителей, кроме 1.
# Число 33, делители: 1, 3, 11, 33
# Число 7, делители: 1, 7.
# Ни один из делителей числа 33 не является делителем числа 7, поэтому числа 7 и 33 взаимно простые.

# вводим и проверяем ключ alpha
checking_flag: bool = True
while checking_flag:
    alpha = input(f'\nВведите ключ alpha.\nТолько взаимно простые элементы с числом {n_mod}: ')
    try:
        alpha = int(alpha)
    except Exception as err:
        print(f'Не удалось привести к int введённые данные, это число? Сообщение: {err}')
        simple_exit()

    print('Проверяем введённый ключ alpha...')
    if is_vzaimno_prostoe(n_mod, alpha) == 1:
        checking_flag = False
        print(f'Числа {n_mod} и {alpha} взаимно простые.')
    else:
        print(f'Числа {n_mod} и {alpha} НЕ взаимно простые, введите иной ключ alpha!')
        continue

# вводим и проверяем ключ beta
beta = checking_beta_key()


# выводим проверку для пользователя
input_user: str = input(f'\nЧто необходимо сделать со данными?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
if input_user == '1':
    pass
elif input_user == '2':
    pass
else:
    simple_exit()








# def crypto_func(our_word: str, alpha_key: int, beta_key: int) -> str:



# прописываем соответствие "буква алфавита - номер"
print('\nПеревод элементов слова для шифрования в арабские цифры.')
numbers_of_letters: list = []
for letter in our_word.lower():
    numbers_of_letters.append(rus_lettet_digit[letter])
print(numbers_of_letters)


# находим список y-ов по ф-ле из раздела "Зашифрование" уi = (alpha * xi + beta) mod n_mod
# # В базовом случае: x1 = (7 * 2 + 14) % 33
crypto_symbols: list = list()
for digit in numbers_of_letters:
    temp_y = (alpha * digit + beta) % n_mod
    crypto_symbols.append(rus_digit_letter[temp_y])

print('\nЗашифрованная фраза:')
pprint(crypto_symbols)


print('\nОсуществляем проверку. С помощью Расширенного алгоритма Евклида найдём обратный элемент.')
reverse_element: int = rae(alpha, n_mod)
print(f'Результат вычисления РАЕ: {reverse_element}')


print('\nПроверяем корректность найденного обратного элемента.')
# Ф-ла: (alpha * alpha**-1) ≡ 1 * mod n_mod
# В базовом случае: 7 * 19 ≡ 1 * mod 33 = 133 ≡ 1 * mod 33 = 133 mod 33 = 1
checking_reverse_element: int = (alpha * reverse_element) % n_mod
if checking_reverse_element == 1:
    print('Проверка пройдена успешно!')
else:
    print('Проверка не пройдена! Завершаем программу...')
    simple_exit()

# Проверяем по ф-ле из раздела "Расшифрование" xi = alpha**-1 * (yi - beta) mod n_mod
print('\nПроверяем элементы зашифрованной фразы.')
elements_check: list = list()
for elem in crypto_symbols:
    temp_x = reverse_element * (rus_lettet_digit[elem] - beta) % n_mod
    elements_check.append(temp_x)

print(elements_check)

# Финал-проверка
final_check: list = list()
print('\nВосстанавливаем исходное слово-фразу:')
for elem in elements_check:
    final_check.append(rus_digit_letter[elem])

our_first_word: str = ''
for elem in final_check:
    our_first_word += elem

print(our_first_word)
if our_first_word == our_word:
    print('Исходное слово-фраза и расшифровоанное совпадают!')
else:
    print('Расшифрованная слово-фраза не совпадает с исходной!')
