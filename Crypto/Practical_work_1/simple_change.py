# Шифр простой замены
from general_store import true_alphabet
from general_store import crypto_alphabet
from general_store import checking_input_word
from general_store import simple_exit


def crypt_func(just_word: str) -> str:
    """Функция зашифрования"""
    print(f'\nАктивируем «Шифр простой замены», результат для слова «{our_word}»:')
    crypto_word: str = ''
    for elem in just_word.lower():
        crypto_word += true_crypto_letters[elem]
    return crypto_word


def uncrypt_func(encode_word: str) -> str:
    """Функция расшифрования"""
    print('\nВыполняем расшифровку, изначальное слово:')
    original_word: str = ''
    for letter in encode_word:
        original_word += crypto_true_letters[letter]
    return original_word


# создаём два словаря для зашифровки и расшифровки
true_crypto_letters: dict = dict(zip(true_alphabet, crypto_alphabet))
crypto_true_letters: dict = dict(zip(crypto_alphabet, true_alphabet))

our_word: str = input('Здравствуй, %username%! \nПожалуйста, введи слово для «Шифра простой замены» (только кириллица).'
                      'Спасибо! \nP.S.: есть базовая проверка ввода: ')

# проверка введённых данных
checking_input_word(our_word)

input_user: str = input(f'\nЧто необходимо сделать с данными?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
if input_user == '1':
    print(crypt_func(our_word))
elif input_user == '2':
    print(uncrypt_func(our_word))
else:
    simple_exit()
