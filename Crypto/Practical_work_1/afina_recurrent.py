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

# длина русского алфавита, из этой длины random можно выбрать beta
n_mod: int = 33

# нам понадобятся дополнительные ключи
alpha_first: int = 7 # взаимно простое с n_mod
beta_first: int = 14 # random число от 0 до 32, нашего n_mod
alpha_second: int = 5 # взаимно простое с n_mod
beta_second: int = 9 # random число от 0 до 32, нашего n_mod

our_word: str = input('\nЗдравствуй, %username%! \nПожалуйста, введи слово для «Аффинного рекуррентныого шифра» '
                      '(только кириллица). Спасибо! \nP.S.: есть базовая проверка ввода: ')

checkin_input_word(our_word)


# Зашифровываем
# прописываем соответствие "буква алфавита - номер"
print('\nПеревод элементов слова для шифрования в арабские цифры.')
numbers_of_letters: list = []
for letter in our_word.lower():
    numbers_of_letters.append(rus_lettet_digit[letter])
print(numbers_of_letters)


# Находим список y-ов по ф-ле из раздела "Зашифрование":
# Формула для у1:
# у1 = (alpha_first * x1 + beta_first) mod n_mod
# # В базовом случае: x1 = (7 * 2 + 14) % 33
crypto_symbols: list = list()
y1 = (alpha_first * numbers_of_letters[0] + beta_first) % n_mod
crypto_symbols.append(rus_digit_letter[y1])

# Формула для y2:
# y2 = (alpha_second * x2 + beta_second) mod n_mod
y2 = (alpha_second * numbers_of_letters[1] + beta_second) % n_mod
crypto_symbols.append(rus_digit_letter[y2])

# Формула для последующих yi: произведение двух предыдущих alpha и сумма двух предыдущих beta (оба по n_mod)
# уi = ((((alpha_first * alpha_second) mod n_mod) * x3) + ((beta_first + beta_second) mod n_mod)) mod n_mod
alpha_third = (alpha_first * alpha_second) % n_mod
beta_third = (beta_first + beta_second) % n_mod

# берём наш список с третьего элемента (т. к. первые два уже ушли для y1 и y2)
for digit in numbers_of_letters[2:]:
    alpha_next = (alpha_second * alpha_third) % n_mod
    beta_next = (beta_second + beta_third) % n_mod

    yi = (alpha_next * digit + beta_next) % n_mod
    crypto_symbols.append(rus_digit_letter[yi])

    # создаём новые значения alpha и beta для текущего цикла на основе предыдущих значений
    alpha_second = alpha_third
    alpha_third = alpha_next

    beta_second = beta_third
    beta_third = beta_next

print('\nЗашифрованная фраза:')
print(crypto_symbols)
