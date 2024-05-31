# Программная реализация ГОСТ 34.10-2012
# https://docs.cntd.ru/document/1200095034?marker
# https://docs.cntd.ru/document/1200095035#7D20K3

import math
from store_gost import rae
# from store_gost import elliptic_points TODO: del
from store_gost import find_simple_q
from store_gost import simple_exit


# Параметры схемы цифровой подписи
# 1
# Простое число p, 256 бит, модуль эллиптической кривой
p: int = 57896044618658097711785492504343953926634992332820282019728792003956564821041
# p: int = 101 TODO: del

# 2
# Эллиптическая кривая E, с параметрами a, b
# Имеет вид: E a,b(Fp)
a: int = 7
b: int = 43308876546767276905765904595650931995942111794451039583252968842033849580414

# Вид нашей эллептической кривой
print(f'Вид нашей эллептической кривой: E{a},{b}(F{p})')


# Уравнение эллептической кривой в общем виде имеет следующий вид:
# у**2 = x**3 + ax + b
print(f'В нашем случае уравнение эллептической кривой имеет вид: у**2 = x**3 + {a}x + {b}')


# Проверяем условие гладкости кривой по формуле:
# (-4a**3 - 27b**2) mod p     НЕ должно быть не равно 0
res: int = ((-4*a**3) - (27*b**2)) % p
print(f'Проверяем условие гладкости эллептической кривой:')
if res != 0:
    print(f'Наше значение: {res}\nУсловие гладкости эллептической кривой выполнено.')
else:
    print(f'Наше значение: {res}\nYсловие гладкости эллептической кривой НЕ ВЫПОЛНЕНО!')
    simple_exit()


# 3
# Целое число m - порядок группы точек эллиптической кривой E, такое, чтобы выполнялось условие:
# p+1-2*math.sqrt(p) <= m <= p+1+2*math.sqrt(p)
print('\nНаходим порядок группы точек эллиптической кривой (округление в большую сторону), переменная m')
# p1_number: int = math.ceil(round(p+1-2*math.sqrt(p)))
# p2_number: int = math.ceil(round(p+1+2*math.sqrt(p)))
p1_number: int = math.ceil(p+1-2*math.sqrt(p))
p2_number: int = math.ceil(p+1+2*math.sqrt(p))

print(f'Порядок группы точек эллиптической кривой: {p1_number} <= m <= {p2_number}')
# TODO: ВСПОМНИТЬ ЭЛЛИПТИЧЕСКИЕ КРИВЫЕ!!!!!!!!!!!!!!!!!!!!!!! Без них не получится. У нас получилось m=112
m: int = 57896044618658097711785492504343953927082934583725450622380973592137631069619
print(f'Число m = {m}')

# TODO: точно del, потому что math.ceil(p+1-2*math.sqrt(p)) и  math.ceil(p+1+2*math.sqrt(p)) даёт одинаковые значения...
# if p1_number <= m <= p2_number:
#     print('Проверка числа m прошла успешна.')
# else:
#     print('Проверка числа m НЕ прошла.')
#     simple_exit()











# Пример использования функции нахождения точек эллиптической кривой TODO: del, если будет не нужна
# a = 4
# b = 1
# x_range = (-28948022309329048855892746252171976963317496166410141009864396001978282410520, 28948022309329048855892746252171976963317496166410141009864396001978282410520)
# points = elliptic_points(a, b, x_range)
# print("Points on the elliptic curve:", points)








# 4
# найдём q - порядок циклической подргуппы группы точек эллиптической кривой
print('\nНайдём q. Которая соответствует условию: m = n*q , где n - натуральное число, q - простое число.')
# В базовом случае m = 112, получается формула: 112 = n * q, т.е. 112 = 16 * 7 (22:19 время!)

q: int = find_simple_q(m)
if q:
    print(f"Простое число q, удовлетворяющее уравнению m = n * q найдено.")
else:
    print(f"Простое число q для {m} не найдено.")
    simple_exit()

print(f'Число q = {q}')

# 5
#  Мы должны найти точку, не являющейся точкой 0 эллиптической кривой, порядком которой является количество сложений q
# Берём конкретную точку для примера
x: int = 2
y: int = 4018974056539037503335449422937059775635739389905545080690979365213431566280
# Убеждаемся, что она действительно принадлежит нашей эллиптической кривой: подставим её координаты в наше уравнение.
# Уравнение эллептической кривой в общем виде имеет следующий вид:
# у**2 = x**3 + ax + b
p_x: int = x**3 + a*x + b
print(f'Результат для точки эллиптической кривой: {p_x}')


# 6
# Хэш-функция.
# Прописана в ГОСТе.

# 7
# Указываем ключ подписи - целое число d
d_signature_key: int = 55441196065363246126355624130324183196576709222340016572108097750006097525544

# 8
# Ключ проверки подписи, это точка эллиптической кривой Q = dP
# В нашем случае Q = dP = 55441196065363246126355624130324183196576709222340016572108097750006097525544P
x1: int = 2
y1: int = 4018974056539037503335449422937059775635739389905545080690979365213431566280

print('\nРасчёт x3 (формула два)')
x3_1: int = ((3*x1**2 + a)**2) % p
x3_2: int = ((2*y1)**2) % p
print(f'Видим результат вычисления: {x3_1} / {x3_2} - {2*x1}')


# временный элемент для расчётов temp_elem_for_x3
temp_elem_for_x3: int = x3_1
for elem in range(1000):
    if (temp_elem_for_x3 % x3_2) == 0:
        print(f'{temp_elem_for_x3} Делится нацело, результат: {temp_elem_for_x3 % x3_2}')
        break
    else:
        # print(f'{temp_elem_for_x3} НЕ делится нацело. Прибавляем к числителю модуль {p}')
        temp_elem_for_x3 += p
print(f'Результат: число, которое делится на цело после прибавления к числителю модуля: {temp_elem_for_x3}')

x3_result: int = (temp_elem_for_x3 // x3_2) - 2*x1
print(f'Обновлённый результат вычисления: {x3_result}')

print(f'Результат вычислений: x3 = {x3_result}')


print('\nРасчёт у3 (формула два)')
y3_1: int = (3*x1**2 + a) % p
y3_2: int = 2*y1 % p
y3_3: int = (x1 - x3_result)


print(f'Данные для расчёта: {y3_1} / {y3_2} * {x1 - x3_result} - {y1}')


# временный элемент для расчётов temp_elem_for_у3
for_raschet_y3: int = y3_1 * y3_3
for elem in range(1000):
    if (for_raschet_y3 % y3_2) == 0:
        print(f'{for_raschet_y3} Делится нацело, результат: {for_raschet_y3 % y3_2}')
        break
    else:
        # print(f'{for_raschet_y3} НЕ делится нацело. Прибавляем к числителю модуль {p}')
        for_raschet_y3 += p
print(f'Результат: число, которое делится на цело после прибавления к числителю модуля: {for_raschet_y3}')

y3_result: int = ((for_raschet_y3 // y3_2) - y1) % p
print(f'Результат вычислений: y3 = {y3_result}')

print(f'Итоговый результат: ({x3_result}, {y3_result})')


print(f'\n\nВычисляем ({x3_result}, {y3_result}) + ({x1}, {y1})')
# точки разные, воспользуемся первой формулой расчёта точек эллиптической кривой

print('\nРасчёт x3 (формула один)')
x1_formula_one: int = x3_result
y1_formula_one: int = y3_result

x2_formula_one: int = x1
y2_formula_one: int = y1
print(f'Подготовленные данные: x1 = {x1_formula_one}, y1 = {y1_formula_one}, x2 = {x2_formula_one}, y2 = {y2_formula_one}')


x3_formula_one: int = ((y2_formula_one - y1_formula_one)**2) % p
x3_2_formula_one: int = ((x2_formula_one - x1_formula_one)**2) % p
print(f'Промежуточный результат: {x3_formula_one} / {x3_2_formula_one} - {x1_formula_one} - {x2_formula_one}')


#TODO: временные расчёты добавить в функцию
# временный элемент для расчётов по формуле один, прибавляем модуль
x_temp_elem_formula_one: int = x3_formula_one
for elem in range(1000):
    if (x_temp_elem_formula_one % x3_2_formula_one) == 0:
        print(f'{x_temp_elem_formula_one} Делится нацело, результат: {x_temp_elem_formula_one % x3_2_formula_one}')
        break
    else:
        # print(f'{temp_elem_for_x3} НЕ делится нацело. Прибавляем к числителю модуль {p}')
        x_temp_elem_formula_one += p
print(f'Результат: число, которое делится на цело после прибавления к числителю модуля: {x_temp_elem_formula_one}')

x3_result_formula_one: int = (x_temp_elem_formula_one // x3_2_formula_one) - x1_formula_one - x2_formula_one
print(f'Результат для формулы 1, x3 = {x3_result_formula_one}')







print('\nРасчёт y3 (формула один)')
y3_formula_one: int = (y2_formula_one - y1_formula_one)
y3_2_formula_one: int = (x2_formula_one - x1_formula_one)
y3_3_formula_one: int = (x1_formula_one - x3_result_formula_one)


print(f'Данные для расчёта: {y3_formula_one} / {y3_2_formula_one} * {y3_3_formula_one} - {y1_formula_one}')

# временный элемент для расчётов y_temp_elem_formula_one
y_temp_elem_formula_one: int = y3_formula_one * y3_3_formula_one
for elem in range(1000):
    if (y_temp_elem_formula_one % y3_2_formula_one) == 0:
        print(f'{y_temp_elem_formula_one} Делится нацело, результат: {y_temp_elem_formula_one % y3_2_formula_one}')
        break
    else:
        # print(f'{for_raschet_y3} НЕ делится нацело. Прибавляем к числителю модуль {p}')
        y_temp_elem_formula_one += p
print(f'Результат: число, которое делится на цело после прибавления к числителю модуля: {y_temp_elem_formula_one}')

y3_result: int = ((y_temp_elem_formula_one // y3_2_formula_one) - y1_formula_one) % p
print(f'Результат вычислений: y3 = {y3_result}')




# Алгоритм формирования подписи
print('\n\n\nАлгоритм формирования подписи')

# TODO: нам потребуется сообщение M - возьмём данные из rsa, там есть перевод текста в двоичный режим.
# Тут сейчас используется тест-переменная:
# 1
print('Вычисляем хэш-код сообщения M по формуле: h = h(M)')
print('Текст из файла.')
file_path = 'check_file.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    base_m_message = file.read()

print(f'Базовое сообщение: {base_m_message}')
m_message = bin(int(base_m_message))[2:]
print(f'Двоичное представление сообщения: {m_message}')


# # данные для хэширования - начало
# import hashlib
#
#
# message: str = 'привет как дела?'
#
# # чистый хеш-код
# mess_byte = message.encode('utf-8')
# hash_obj = hashlib.sha256(mess_byte)
# hash_code = hash_obj.hexdigest()
#
# print(f'Хэш-код сообщения {message}: {hash_code}')
#
#
# # бинарный формат
# hash_code_binary = hashlib.sha256(message.encode()).digest()
# print(type(hash_code_binary))
# print(hash_code_binary)
#
#
# # в виде 0 и 1
# hash_code_zero_one = hashlib.sha256(message.encode()).hexdigest()
# binary_hash_code = ''.join(format(int(x, 16), '08b') for x in hash_code_zero_one)
# print(f'0-1: {binary_hash_code}')

# hash_code_1 = 1302397928
# final_message = ''
# while hash_code_1 > 0:
#     final_message = chr(hash_code_1 % 256) + final_message
#     hash_code_1 = hash_code_1 // 256
#
# print(final_message)

# данные для хэширования - окончание



# Выясняем, с каким размером подписи мы работаем в нашем примере. Для этого определяем битовую длину q
q_length_bits: int = q.bit_length()
# [2:] отсекаем через [2:] начало 0b
q_binary = bin(q)[2:]
print(f'Битовая длина q (число {q}) равна: {q_length_bits} бит(а), значение в двоичном виде: {q_binary}')
print(f'Значит, для хеширования мы будем разделять нашу последовательность на блоки по {q_length_bits} бит(а).')
print(f'Выполняем хеширование для этого разделяем последовательность {m_message} число на блоки по {q_length_bits} бит(а).')

temp_list = []
# создаём список элементов из сообщения длиной q бит
for elem in range(len(m_message)):
    temp_list.append(m_message[-q_length_bits:])
    m_message = m_message[:-q_length_bits]

# убираем "пустые" элементы ''
temp_list = list(filter(bool, temp_list))
# переворачиваем список
temp_list = temp_list[::-1]
print(f'Базовый список: {temp_list}')

# дополняем нулями значения списка
# создаём список, у которого будет заполнение нулями в первом элементе
null_list = temp_list
for l_elem in temp_list:
    if len(l_elem) < q_length_bits:
        l_elem = ('0'*(q_length_bits-len(l_elem))) + l_elem
        # print(f'New elem: {l_elem}')
        null_list[0] = l_elem

print(f'Итоговый список с заполненными нулями: {null_list}')

sum_list_elements: int = 0
for elem in null_list:
    sum_list_elements += int(elem)

final_sum_list_elements = bin(sum_list_elements)[2:]
print(f'Результат сложения "кусочков" хеша: {final_sum_list_elements}')
q_bytes_peace = final_sum_list_elements[-q_length_bits:]
print(f'Берём младшие {q_length_bits} бита результата в качестве подписи, результат: {q_bytes_peace}')
print(f'Итог Шага 1 Алгоритма формирования подписи. Наша подпись: h = h(M) = {q_bytes_peace}')


print('\nШаг 2, Алгоритм формирования подписи')
# Вычисляем a, двоичным представлением которого является вектор h
# Определить e = a (mod q). Если e = 0, то определить e = 1
a = int(q_bytes_peace, 2)
print(f'В двоичном представлении {q_bytes_peace} это a = {a} в десятичном виде.')

e = a % q
print(f'e равное a ({a}) по модулью q ({q}), результат e = {e}')

# если e == 0, то e присваиваем 1
if e == 0:
    print(f'e = {e}, присваиваем e значение 1')
    e: int = 1


print('\nШаг 3, Алгоритм формирования подписи')
print(f'Генерируем число 0 < k < {q}')

# TODO: del генерируем случайно число: import random k = random.randint(0, q, в примере 7)
from random import randint
k: int = randint(0, q)



print('\nШаг 4, Алгоритм формирования подписи')
print(f'Вычислить точку эллиптической кривой C = {k}P')
# dot_p: tuple = (37, 10)
dot_p: tuple = (57520216126176808443631405023338071176630104906313632182896741342206604859403, 17614944419213781543809391949654080031942662045363639260709847859438286763994)

r: int = dot_p[0] % q

# TODO: del
# print(r)
# print(type(r))
# print(len(str(r)))

print(f'Найдём r малое по формуле: x данной точки по mod {q}, результат r = {r}')
if r == 0:
    from random import randint
    print('Проходим заново Шаг 3 и Шаг 4')
    k = randint(0, q)


print('\nШаг 5, Алгоритм формирования подписи')
print(f'Вычисляем s = ({r} * {d_signature_key} + {k} * {e}) mod {q}')
s: int = (r * d_signature_key + k * e) % q
print(f's = {s}') # TODO: del

if s == 0:
    print('Проходим заново Шаг 3 и Шаг 4!')


print('\nШаг 6, Алгоритм формирования подписи')
print('Вычисляем двоичные векторы r и s, и через их конкатинацию вычисляем цифровую подпись')

print('Вычисляем r (в бинарном виде)')
r_binary = bin(r)[2:]
# дополняем значение нулями слева
if len(str(r_binary)) < q_length_bits:
    r_binary = ('0' * (q_length_bits - len(str(r_binary)))) + str(r_binary)
print(f'r в десятичном виде: {r}, в двоичном виде: {r_binary}')

print('Вычисляем s (в бинарном виде)')
s_binary = bin(s)[2:]
# дополняем значение нулями слева
if len(str(s_binary)) < q_length_bits:
    s_binary = ('0' * (q_length_bits - len(str(s_binary)))) + str(s_binary)
print(f's в десятичном виде: {s}, в двоичном виде: {s_binary}')

r_bin_and_s_bin = r_binary + s_binary
print(f'Электронная подпись, связка r||s = {r_bin_and_s_bin}')




print('\n\n\nАлгоритм проверки подписи')
print('Шаг 1, Алгоритм проверки подписи')
print(f'По полученной подписи {r_bin_and_s_bin} вычисляем целые числа r и s')
print(type(r_bin_and_s_bin)) # TODO: del

# из электронной подписи берём данные в соответствии с битовой длиной q и переводим в десятичное представление
r_ressurection = int(r_bin_and_s_bin[:q_length_bits], 2)
s_ressurection = int(r_bin_and_s_bin[q_length_bits:], 2)
print(f'Число r = {r_ressurection}, число s = {s_ressurection}')

print('Проводим "быструю проверку", что r и s попадают в нужные промежутки по формулам: 0 < r < q и 0 < s < q')

if (0 < r < q):
    print(f'r = {r} и попадает в нужный промежуток.')
else:
    print(f'r = {r} и НЕ попадает в нужный промежуток.')

if (0 < s < q):
    print(f's = {s} и попадает в нужный промежуток.')
else:
    print(f's = {s} и НЕ попадает в нужный промежуток.')


print('\nШаг 2, Алгоритм проверки подписи')
print('Наше исходное сообщение в открытом виде (или зашифровано) доступно, а подпись к нему присоединена.')
print('Т.е. мы можем взять это сообщение и получить его хеш-код.')
print('Рассматриваем случай, когда никаких изменений в сообщение не было внесено. Оно без изменений. Поэтому хеш-код сообщения совпадает')
print(f'Наша текущая подпись h(M) = {q_bytes_peace}')


print('\nШаг 3, Алгоритм проверки подписи')
a_check_sig: int = int(q_bytes_peace, 2)
print(f'Найдём целое число a, десятичное представление которого вектор h({q_bytes_peace}).\n Результат a = {a_check_sig}')

print('Определим число e по формуле: e = a(mod q), если e = 0, то e = 1')
e_check_sig: int = a_check_sig % q
if e_check_sig == 0:
    e_check_sig = 1
print(f'Результат: число e = {e_check_sig}')


print('\nШаг 4, Алгоритм проверки подписи')
print(f'Вычисляем значение v по формуле: v = e**-1 mod {q}. Воспользуемся РАЕ.')
v = rae(e_check_sig, q)
print(f'Результат после РАЕ: v = {v}')


print('\nШаг 5, Алгоритм проверки подписи')
print('Вычисляем значения по формулам: z1 = s * v (mod q) и z2 = -r * v (mod q)')
z1_check = (s * v) % q
z2_check = (-r * v) % q
print(f'Результаты: z1 = {z1_check}, z2 = {z2_check}')


print('\nШаг 6, Алгоритм проверки подписи')
print('Вычисляем точку эллиптической кривой по формуле: C = z1P + z2Q')
print('Также определяем R = x * c (mod q)')
print(f'C = {z1_check}P + {z2_check}Q, в нашем случае мы посчитали, что Q = 3P, значит, С = 4P + 6P = 10P.')
print('10P можно разделить на 7P + 3P. Т. к. 7 - порядок подгруппы, с которой мы работаем, то точка 7P = 0, а значение 3P известно (37, 10)')

print('Вычисляем R')
r_big = x3_result_formula_one % q
print(f'R = {r_big}')
print(f'r = {r}')
print(f'res = {r_ressurection}')

print('\nШаг 7, Алгоритм проверки подписи')
print('Проверка статуса подписи.')
if r_big == r:
    print('Подпись принята!')
else:
    print('Подпись неверна.')
