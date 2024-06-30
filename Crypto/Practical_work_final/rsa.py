from store_rsa import is_simple_number
from store_rsa import get_check_e
from store_rsa import rae
from store_rsa import encrypt_message
from store_rsa import decrypt_message
from store_rsa import simple_exit


# слово для шифрования
code_string: str = 'ЛЕС'
print(f'Нужно зашифровать алгориитмом RSA слово: {code_string}')
print('\nАлгоритм генерации ключей')
# Простое число - это натуральное число > 1, которое делится без остатка на 1 и на себя.
print('Шаг 1, Генерация ключей, простые числа p и q, причём p - q = большое число.')

key_p: int = 109
key_q: int = 71
print(f'Выбираем простое число p:  {key_p}')
print(f'Выбираем простое число q:  {key_q}')

print('\nШаг 2, вычисляем модуль алгоритма n = p * q')
n: int = key_p * key_q
print(f'Вычисляем по формуле n = p * q, n: {n}')


print('\nШаг 3, вычисляем значение ф-ии Эйлера для n, по ф-ле: f(n) = (p - 1) * (q - 1)')
ayler_function_result: int = (key_p - 1) * (key_q - 1)
print(f'Вычисляем значение функции Эйлера f(n): {ayler_function_result}')


print('\nШаг 4, выбираем экспоненту зашифрования - это целое число e, взаимно простое со значением f(n)')
number_e: int = get_check_e(ayler_function_result)
print(f'Результат, число e: {number_e}')


print('\nШаг 5, находим экспоненту расшифрования - это целое число d, удовлетворяющее соотношению: e * d ≡ 1(mod f(n)\n находим d с помощью РАЕ')
# в базовом случае это: d = e**-1 mod f(n), d = 13**-1 mod 7560
# находим d с помощью РАЕ
d = close_key = rae(number_e, ayler_function_result)
print(f'Результат, число d (закрытый ключ): {d}')


print('Шаг 6, у нас есть пара e, n - это открытый ключ, d - закрытый ключ')
open_key: list = [number_e, ayler_function_result]
print(f'Итог по ключам. Открытый ключ: {open_key}.\nЗакрытый ключ: {close_key}')


# Выбор пользователя: зашифровать или расшифровать
input_user: str = input(f'\nЧто необходимо сделать?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
if input_user == '1':
    print('\n Порядок Зашифровывания.')
    print('\nШаг 1, Боб получает аутентичную копию открытого ключа Алисы: e и n')
    crypted_message_bin: list = encrypt_message(n, code_string, number_e)
    print('\nШифроТекст: ')
    print(''.join(crypted_message_bin))

# расшифрование на экзамене не использовалось, тут нужны ещё файлы, которые есть в Практической 2
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
