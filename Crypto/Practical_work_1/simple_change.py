# Шифр простой замены
from time import sleep


true_alphabet: list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',
                       'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
crypto_alphabet: list = ['б', 'а', 'г', 'в', 'е', 'д', 'ж', 'ё', 'и', 'з', 'к', 'й', 'м', 'л', 'о', 'н', 'р', 'п', 'т',
                         'с', 'ф', 'у', 'ц', 'х', 'ш', 'ч', 'ъ', 'щ', 'ь', 'ы', 'я', 'э', 'ю']

# для проверки корректного ввода, английский алфавит и спецсимволы
eng_alphabet_spec: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'i',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(',
                           ')', '_', '+', '-', '"', '№', ';', ':', '?', '<', '>', ',' '.', '/', '\\', '|', '', '~',
                           '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# оздаём два словаря для зашифровки и расшифровки
true_crypto_lettsrs: dict = dict(zip(true_alphabet, crypto_alphabet))
crypto_true_letters: dict = dict(zip(crypto_alphabet, true_alphabet))


# ф-ия выхода
def simple_exit():
    print('\nВведены предосудительные символы!\nПожалуйста, запустите программу заново и выполните корректный ввод!')
    exit()


our_word: str = input('Здравствуй, %username%! \nПожалуйста, введи слово, которое состоит из русских (кириллица) букв! '
                      'Спасибо! \nP.S.: есть базовая проверка ввода: ')

print('\nПроверочная фаза, пожалуйста, подождите...')
sleep(1)
if len(our_word) == 0:
    simple_exit()

for key in our_word:
    print(f'\nТщательно проверяем символ: {key}')
    if (len(key) == 0) or (key in eng_alphabet_spec):
        simple_exit()

print(f'\nАктивируем шифр простой замены, результат для слова «{our_word}»:')
crypto_word: str = ''
for letter in our_word.lower():
    crypto_word += true_crypto_lettsrs[letter]

print(crypto_word)

print('\nВыполняем расшифровку, изначальное слово:')
original_word: str = ''
for letter in crypto_word:
    original_word += crypto_true_letters[letter]

print(original_word)
