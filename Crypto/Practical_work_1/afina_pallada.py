# Аффинный шифр
# Шифр подстановочный. Криптографическое преобразование заменяет символы открытого текста на другие по правилу.
# Базовые данные: вфеврале, альфа: 7, бета: 14
from general_store import checkin_input_word
from general_store import is_vzaimno_prostoe
from general_store import crypt_func
from general_store import uncrypt_func
from general_store import checking_beta_key
from general_store import simple_exit


# длина русского алфавита
n_mod: int = 33

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

# получаем и проверяем ключ alpha
checking_flag: bool = True
while checking_flag:
    try:
        alpha = int(input(f'\nВведите ключ alpha.\nТолько взаимно простые элементы с числом {n_mod}: '))
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
input_user: str = input(f'\nЧто необходимо сделать?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
if input_user == '1':
    crypto_phrase = crypt_func(our_word, alpha, beta, n_mod)
    print('\nЗашифрованная фраза: ')
    print(''.join(crypto_phrase))
elif input_user == '2':
    uncrypted_word: list = uncrypt_func(our_word, alpha, beta, n_mod)
    print('\nРасшифрованная фраза: ')
    print(''.join(uncrypted_word))
else:
    simple_exit()
