from store_rsa import is_simple_number
from store_rsa import get_check_e
from store_rsa import rae
from store_rsa import encrypt_message
from store_rsa import decrypt_message
from store_rsa import simple_exit


# Генерация ключей, простые числа p и q, причём p - q = большое число.
# Простое число - это натуральное число > 1, которое делится без остатка на 1 и на себя.
# Шаг 1
# key_p: int = int(input('Введите ключ p, условие: это должно быть простое число: '))
# if is_simple_number(key_p):
#     print(f'{key_p} - простое число')
# else:
#     print(f'{key_p} - НЕ простое число')
#     simple_exit()
#
# key_q: int = int(input('Введите ключ q, условие: это должно быть простое число: '))
# if is_simple_number(key_q):
#     print(f'{key_q} - простое число')
# else:
#     print(f'{key_q} - НЕ простое число')
#     simple_exit()

# TODO: del, раскомменить то, что выше
key_p = 33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489
key_q = 115792089210356248762697446949407573530086143415290314195533631308867097853951
# key_p = 109
# key_q = 71


# Шаг 2, вычисляем n = p * q
n: int = key_p * key_q
print(f'Вычисляем по формуле n = p * q, n: {n}')

# Шаг 3, вычисляем значение ф-ии Эйлера для n, по ф-ле: f(n) = (p - 1) * (q - 1)
ayler_function_result: int = (key_p - 1) * (key_q - 1)
print(f'Вычисляем значение функции Эйлера f(n): {ayler_function_result}')


# Шаг 4, выбираем экспоненту зашифрования - это целое число e, взаимно простое со значением f(n)
number_e: int = get_check_e(ayler_function_result)
print(f'Результат, число e: {number_e}')


# Шаг 5, находим экспоненту расшифрования - это целое число d, удовлетворяющее соотношению: e * d ≡ 1(mod f(n)
# в базовом случае это: d = e**-1 mod f(n), d = 13**-1 mod 7560
# находим d с помощью РАЕ
d = close_key = rae(number_e, ayler_function_result)
print(f'Результат, число d (закрытый ключ): {d}')


# Шаг 6, у нас есть пара e, n - это открытый ключ, d - закрытый ключ
open_key: list = [number_e, ayler_function_result]
print(f'Итог по ключам. Открытый ключ: {open_key}.\nЗакрытый ключ: {close_key}')


# Выбор пользователя: зашифровать или расшифровать
input_user: str = input(f'\nЧто необходимо сделать?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
if input_user == '1':
    print('Выгружаем текст из файла.')
    file_path = 'encrypt.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        code_string = file.read()
    crypted_message_bin: list = encrypt_message(n, code_string, number_e)
    print('\nШифроТекст: ')
    print(''.join(crypted_message_bin))

elif input_user == '2':
    print('Выгружаем ШифроТекст из файла.')
    file_path = 'decrypt.txt'
    list_for_decrypt: list = []
    with open(file_path, 'r') as file:
        for line in file:
            # Удаляем лишние кавычки и пробелы в списке
            list_for_decrypt.extend(line.strip().replace("'", "").split(', '))
    uncrypted_message = decrypt_message(n, list_for_decrypt, d)

else:
    simple_exit()
