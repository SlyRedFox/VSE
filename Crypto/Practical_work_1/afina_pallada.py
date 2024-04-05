# Аффинный шифр
# Шифр подстановочный. Криптографическое преобразование заменяет символы открытого текста на другие по правилу.
# Базовые данные: вфеврале, альфа: 7, бета: 14
from general_store import checking_input_word
from general_store import crypt_func
from general_store import uncrypt_func
from general_store import get_check_beta_key
from general_store import get_check_alpha_key
from general_store import simple_exit


# длина русского алфавита
n_mod: int = 33

# запрос ввода данных от пользователя
our_word: str = input('\nЗдравствуйте, %username%! \nПожалуйста, введите слово (или несколько без пробелов) для'
                      ' «Аффинного шифра» (только кириллица). Спасибо! \nP.S.: есть базовая проверка ввода: ')

# проверка введённых данных
checking_input_word(our_word)

# alpha_key может относиться только к группе обратимых элементов кольца класса вычетов.
# Это элементы, которые взаимно простые с числом n_mod, т. е. те, у которых НОД с n_mod = 1
# Пример:
# Число 7 взаимно простое с 33, т.к. у них разные простые множители, и они не имеют общих делителей, кроме 1.
# Число 33, делители: 1, 3, 11, 33
# Число 7, делители: 1, 7.
# Ни один из делителей числа 33 не является делителем числа 7, поэтому числа 7 и 33 взаимно простые.

# вводим и проверяем ключ alpha_key
alpha_key: int = get_check_alpha_key(n_mod)

# вводим и проверяем ключ beta_key
beta_key: int = get_check_beta_key()


# "перекрёсток" для пользователя
input_user: str = input(f'\nЧто необходимо сделать?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
if input_user == '1':
    crypto_phrase = crypt_func(our_word, alpha_key, beta_key, n_mod)
    print('\nЗашифрованная фраза/слово: ')
    print(''.join(crypto_phrase))
elif input_user == '2':
    uncrypted_word: list = uncrypt_func(our_word, alpha_key, beta_key, n_mod)
    print('\nРасшифрованная фраза/слово: ')
    print(''.join(uncrypted_word))
else:
    simple_exit()
