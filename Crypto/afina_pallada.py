# Афинный шифр, Python-воплощение
# Шифр подстановочный. Криптографическое преобразование заменяет символы открытого текста на другие по правилу.
from pprint import pprint


arabian_digits: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
rus_alphabet: list = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# TODO: del
# digits_eng: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
eng_alphabet: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'i', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
eng_lettet_digit: dict = dict(zip(eng_alphabet, arabian_digits))
# print(eng_lettet_digit)

# словарь {буква: цифра}
rus_lettet_digit: dict = dict(zip(rus_alphabet, arabian_digits))
# словарь {цифра: буква}
rus_digit_letter: dict = dict(zip(arabian_digits, rus_alphabet))
print(rus_lettet_digit)


# TODO добавить input() введите слово для зашифровки Афинным шифром. Сейчас просто слово.
word_encrypt: str = 'вфеврале'

# прописываем соответствие "буква алфавита - номер"
print('\nПеревод элементов слова для шифрования в арабские цифры.')
numbers_of_letters: list = []
for letter in word_encrypt:
    numbers_of_letters.append(rus_lettet_digit[letter])
# 2, 21, 5, 2, 17, 0, 12, 5 (это х1, х2 ... хn)
print(numbers_of_letters)


# TODO: del Задаём ключ. Это пара чисел alpha и beta, которые принадлежат кольцу класса вычетов пункта "ключ" 7:00
# длина rus алфавита, из этой длины random можно выбрать beta
n: int = 33

# alpha может относиться только к группе обратимых эл-ов кольца класса вычетов.
# Это эл-ты, которые взаимно простые с числом n, т. е. те, у которых НОД с n = 1
# Число 7 взаимно простое с 33, т.к. у них разные простые множители, и они не имеют общих делителей, кроме 1.
# Число 33, делители: 1, 3, 11, 33
# Число 7, делители: 1, 7.
# Ни один из делителей числа 33 не является делителем числа 7. Это означает, что число 7 и число 33 взаимно простые.
# TODO del - подбор можно сделать через 4_rae.py, если в Checking 1, подходит
alpha: int = 7
beta: int = 14 # random число от 0 до 32, нашего n

# находим список y-ов по ф-ле из раздела "Зашифрование" уi = (alpha * xi + beta) mod n
# x1 = (7 * 2 + 14) % 33
crypto_symbols: list = list()
for digit in numbers_of_letters:
    temp_y = (alpha * digit + beta) % n
    crypto_symbols.append(rus_digit_letter[temp_y])

print('\nЗашифрованная фраза:')
pprint(crypto_symbols)

print('\nОсуществляем проверку. Воспользуемся сначала Расширенным Алгоритмом Евклида для нахождения обратного эл-та.')
# TODO: внедрить 4_rae.py результат: 7**-1 mod 33 = 19

print('\nПроверяем корректность найденного обратного эл-та.')
# Ф-ла: (alpha * alpha**-1) ≡ 1 * mod n
# В нашем случае: 7 * 19 ≡ 1 * mod 33 = 133 ≡ 1 * mod 33 = 133 mod 33 = 1

# Проверяем по ф-ле из раздела "Расшифрование" xi = alpha**-1 * (yi - beta) mod n = 19 * ()
print('\nПроверяем элементы зашифрованной фразы.')
elements_check: list = list()
for elem in crypto_symbols:
    temp_x = 19 * (rus_lettet_digit[elem] - beta) % n
    elements_check.append(temp_x)

print(elements_check)

# Финал-проверка
final_check: list = list()
print('\nВосстанавливаем исходную фразу.')
for elem in elements_check:
    final_check.append(rus_digit_letter[elem])

our_first_word: str = ''
for elem in final_check:
    our_first_word += elem

# TODO: посмотреть описание Афинного шифра в задании
print(our_first_word)
