# Аффинный рекуррентный шифр
# Базовое слово: вфеврале, значения ключей: альфа1 = 7, альфа2 = 5; бета1 = 14, бета2 = 9
from general_store import arabian_digits
from general_store import checking_input_word
from general_store import true_alphabet
from general_store import get_check_beta_key
from general_store import get_check_alpha_key
from general_store import crypt_afina_recurr
from general_store import uncrypt_afina_recurr
from general_store import simple_exit


# словарь {буква: цифра}
rus_lettet_digit: dict = dict(zip(true_alphabet, arabian_digits))
# словарь {цифра: буква}
rus_digit_letter: dict = dict(zip(arabian_digits, true_alphabet))

# длина русского алфавита
n_mod: int = 33

our_word: str = input('\nЗдравствуйте, %username%! \nПожалуйста, введите слово (или несколько без пробелов) для'
                      ' «Аффинного рекуррентныого шифра» (только кириллица). Спасибо! \nP.S.: есть проверка ввода: ')

# проверка введённых данных
checking_input_word(our_word)

print('\nВвод и проверка ПЕРВОГО ключа alpha.')
alpha_first_key: int = get_check_alpha_key(n_mod)
print('\nВвод и проверка ВТОРОГО ключа alpha.')
alpha_second_key: int = get_check_alpha_key(n_mod)

print('\nВвод и проверка ПЕРВОГО ключа beta.')
beta_first_key: int = get_check_beta_key()
print('\nВвод и проверка ВТОРОГО ключа beta.')
beta_second_key: int = get_check_beta_key()

# создаём списки всех alpha и beta для последующей расшифровки
alpha_list: list = [alpha_first_key, alpha_second_key]
beta_list: list = [beta_first_key, beta_second_key]


# выбор пользователя
input_user: str = input(f'\nЧто необходимо сделать?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
if input_user == '1':
    crypto_phrase = crypt_afina_recurr(n_mod, our_word, alpha_list, beta_list, alpha_first_key, alpha_second_key, beta_first_key, beta_second_key)
    print('\nЗашифрованная фраза/слово: ')
    print(''.join(crypto_phrase))
elif input_user == '2':
    uncrypted_word: list = uncrypt_afina_recurr(n_mod, our_word, alpha_list, beta_list, alpha_first_key, alpha_second_key, beta_first_key, beta_second_key)
    print('\nРасшифрованная фраза/слово: ')
    print(''.join(uncrypted_word))
else:
    simple_exit()
