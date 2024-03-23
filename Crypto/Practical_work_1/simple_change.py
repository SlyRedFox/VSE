# Шифр простой замены
from general_store import true_alphabet
from general_store import crypto_alphabet
from general_store import checkin_input_word


# создаём два словаря для зашифровки и расшифровки
true_crypto_lettsrs: dict = dict(zip(true_alphabet, crypto_alphabet))
crypto_true_letters: dict = dict(zip(crypto_alphabet, true_alphabet))

our_word: str = input('Здравствуй, %username%! \nПожалуйста, введи слово для «Шифра простой замены» (только кириллица).'
                      'Спасибо! \nP.S.: есть базовая проверка ввода: ')

checkin_input_word(our_word)

print(f'\nАктивируем «Шифр простой замены», результат для слова «{our_word}»:')
crypto_word: str = ''
for letter in our_word.lower():
    crypto_word += true_crypto_lettsrs[letter]

print(crypto_word)

print('\nВыполняем расшифровку, изначальное слово:')
original_word: str = ''
for letter in crypto_word:
    original_word += crypto_true_letters[letter]

print(original_word)
