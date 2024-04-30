from store_rsa import is_simple_number
from store_rsa import get_check_e
from store_rsa import rae
from store_rsa import encrypt_message
from store_rsa import decrypt_message
from store_rsa import simple_exit


# Генерация ключей, простые числа p и q, причём p - q = большое число.
# Простое число - это натуральное число > 1, которое делится без остатка на 1 и на себя.
# Шаг 1
key_p: int = int(input('Введите ключ p, условие: это должно быть простое число: '))
if is_simple_number(key_p):
    print(f'{key_p}')
    print('Это простое число.')
else:
    print(f'{key_p}')
    print('Это НЕ простое число.')
    simple_exit()

key_q: int = int(input('Введите ключ q, условие: это должно быть простое число: '))
if is_simple_number(key_q):
    print(f'{key_q}')
    print('Это простое число.')
else:
    print(f'{key_q}')
    print('Это НЕ простое число.')
    simple_exit()

# TODO: del
# key_p = 27092006011010341514027420829757406897815492988089374724674081670153850238608406044492897514241500701494792150161496019313283609741990905773528825001869472960850542479909810496639254801282738207148734457881068870276147021883263816380753512538483942826060812318998243713359552598919875518389304658524957340874495577900416298224827282760801229831372549535596284275510926566245013786273957943656170740444232705681072489272719181287865363163523227227876697008814739615828512463966011777483542337880794243695623851236287591610039790168799222905601449348869229888680394024471436313520162379292429481684430258295928294583117
# key_q = 10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087


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
