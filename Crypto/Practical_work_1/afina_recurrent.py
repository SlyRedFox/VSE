# Аффинный рекуррентный шифр
# Базовое слово: вфеврале
from pprint import pprint
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


# Зашифровыываем @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# прописываем соответствие "буква алфавита - номер"
print('\nПеревод элементов слова для шифрования в арабские цифры.')
numbers_of_letters: list = []
for letter in our_word.lower():
    numbers_of_letters.append(rus_lettet_digit[letter])
print(numbers_of_letters)


# находим список y-ов по ф-ле из раздела "Зашифрование":
# у1 = (alpha_first * xi + beta_first) mod n_mod
# # В базовом случае: x1 = (7 * 2 + 14) % 33
# y2 уже считаем по иной формуле:
# y2 = (alpha_second * xi + beta_second) mod n_mod
crypto_symbols: list = list()
for digit in numbers_of_letters:
    if numbers_of_letters.index(digit) % 2 == 0:
        temp_chetnoe = (alpha_first * digit + beta_first) % n_mod
        crypto_symbols.append(rus_digit_letter[temp_chetnoe])
    elif numbers_of_letters.index(digit) % 2 == 1:
        temp_nechetnoe = (alpha_second * digit + beta_second) % n_mod
        crypto_symbols.append(rus_digit_letter[temp_nechetnoe])

print('\nЗашифрованная фраза:')
pprint(crypto_symbols)
