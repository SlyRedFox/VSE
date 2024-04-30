from store_rsa import is_simple_number
from store_rsa import get_check_e
from store_rsa import rae
from store_rsa import encrypt_message
from store_rsa import decrypt_message
from store_rsa import simple_exit


print('Выгружаем текст из файла.')
# TODO: del, это будет из файла
# code_string: str = 'code'
file_path = 'info.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    code_string = file.read()


# Генерация ключей, простые числа p и q, причём p - q = большое число.
# Простое число - это натуральное число > 1, которое делится без остатка на 1 и на себя.
# Шаг 1
key_p: int = int(input('Введите ключ p, условие: это должно быть простое число: '))
if is_simple_number(key_p):
    print(f'{key_p} - простое число')
else:
    print(f'{key_p} - НЕ простое число')
    simple_exit()

key_q: int = int(input('Введите ключ q, условие: это должно быть простое число: '))
if is_simple_number(key_q):
    print(f'{key_q} - простое число')
else:
    print(f'{key_q} - НЕ простое число')
    simple_exit()

# TODO: del, раскомменить то, что выше
# key_p = 133229759844004487482708555880249346678626057474261077205864389183023234861364418208777584075829137333043610416417327124524498586245925009058056752703032255629359981668770065215708910518156720936777111085351946863259532549531073734735968309756177234860907402402866911980750327039096654624175735120977873540602065705110188565836084476970898796700119815336665449367259897898474051541191386333365997629482539035331856995063593412721362058739238481971311279273609290526805816291683012869780399692407
# key_q = 133294399882575758380143779458803658621711224322668460285458826191727627667054255404674269333491950155273493343140718228407463573528003686665212740575911870128339157499072351179666739658503429931021985160714113146720277365006623692721807916355914275519065334791400296725853788916042959771420436564784273910949
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
# TODO: del, в нашем случае это: d = e**-1 mod f(n), d = 13**-1 mod 7560
# находим d с помощью РАЕ
d = close_key = rae(number_e, ayler_function_result)
print(f'Результат, число d (закрытый ключ): {d}')


# Шаг 6, у нас есть пара e, n - это открытый ключ, d - закрытый ключ
open_key: list = [number_e, ayler_function_result]
print(f'Итог по ключам. Открытый ключ: {open_key}. Закрытый ключ: {close_key}')


# Выбор пользователя: зашифровать или расшифровать
input_user: str = input(f'\nЧто необходимо сделать?\n1. Зашифровать.\n2. Расшифровать.\nСделайте выбор: ')
if input_user == '1':
    crypted_message_bin: list = encrypt_message(n, code_string, number_e)
    print('\nЗашифрованная фраза/слово: ')
    print(''.join(crypted_message_bin))
elif input_user == '2':
    uncrypted_message = decrypt_message(n, code_string, d)
    # print('\nРасшифрованная фраза/слово: ')
    # print(''.join(uncrypted_word))
else:
    simple_exit()
