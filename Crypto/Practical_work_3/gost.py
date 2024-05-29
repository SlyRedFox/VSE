# Программная реализация ГОСТ 34.10-2012

import math


# Параметры схемы цифровой подписи
# 1
# Простое число p модуль эллиптической кривой
p: int = 101

# 2
# Эллиптическая кривая E, с параметрами a, b
# Имеет вид: E a,b(Fp)
a: int = 4
b: int = 1

# Вид нашей эллептической кривой
print(f'Вид нашей эллептической кривой: E{a},{b}(F{101})')


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


# 3
# Целое число m - порядок группы точек эллиптической кривой E, такое, чтобы выполнялось условие:
# p+1-2*math.sqrt(p) <= m <= p+1+2*math.sqrt(p)
print('\nНаходим порядок группы точек эллиптической кривой (округление в большую сторону), переменная m')
p1_number: int = math.ceil(round(p+1-2*math.sqrt(p)))
p2_number: int = math.ceil(round(p+1+2*math.sqrt(p)))
print(f'Порядок группы точек эллиптической кривой: {p1_number} <= m <= {p2_number}')

print('Найдём же m')

# TODO: ВСПОМНИТЬ ЭЛЛИПТИЧЕСКИЕ КРИВЫЕ!!!!!!!!!!!!!!!!!!!!!!! Без них не получится. У нас получилось m=112
m = 112

# 4
# найдём q - порядок циклической подргуппы группы точек эллиптической кривой
print('\nНайдём q. Точку, которая после семи сложений друг с другом даст нам в результате точку 0')
# q соответствует условию: m = n*q , где n - натуральное число. При этом q - простое число.
# Т. к. в нашем случае m = 112, то у нас получается ф-ла:
# 112 = n * q, т.е. 112 = 16 * 7
# 22:19 время!
q: int = 7

# 5
#  Мы должны найти точку, не являющейся точкой 0 эллиптической кривой, порядком которой является количество сложений q (7)
# Берём конкретную точку для примера: P = (4, 9)
x: int = 4
y: int = 9
# Убеждаемся, что она действительно принадлежит нашей эллиптической кривой: подставим её координаты в наше уравнение.
# Уравнение эллептической кривой в общем виде имеет следующий вид:
# у**2 = x**3 + ax + b
p_x: int = x**3 + a*x + b
print(f'Результат для точки эллиптической кривой: {p_x}')

# У нас получилось 81. В этом случае не нужно строить табицу квадратов, т. к. 81 - это таблица квадратов: +9 и -9, т.е.
# корень из 81 это +-9 , а значит уравнению нашей эллиптической кривой F101 данная точка удовлетворяет, т.к. у нас там
# значения от 1 до 50 и от -1 до -50.
# Мы убедились, что точка принадлежит кривой Е.

# Но этого недостаточно, нужно убедиться, что порядок данной точки равен 7. O(P) = 7!

# 6
# Хэш-функция.
# Прописана в ГОСТе.

# 7
# Указываем ключ подписи - целое число d
d_signature_key: int = 3

# 8
# Ключ проверки подписи, это точка эллиптической кривой Q = dP
# т.к. d (d_signature_key) = 3, то в нашем случае Q = dP = 3P, а чтобы найти 3P нужны расчёты.
# Точка P известна, поэтому нам нужно получить точку 2P, чтобы получить 3P
# есть точка P, равная (4, 9), значит, 2P = P + P, у нас для этого есть формулы расчёта эллиптической кривой.
# точки одинаковые, поэтому воспользуемся второй формулой расчёта точек эллиптической кривой
x1: int = 4
y1: int = 9

print('\nРасчёт x3 (формула два)')
x3_1: int = ((3*x1**2 + a)**2) % p
x3_2: int = ((2*y1)**2) % p
print(f'Видим результат вычисления 2P: {x3_1} / {x3_2} - {2*x1}')
# Результат будет (78 / 21) - 8
# Этот результат можно сократить на три, чтобы получилось (26 / 7) - 8, т.к. 26 не делится нацело на 7, то мы должны
# добавлять модуль (у нас это 101) в числитель до тех пор, пока не будет целочисленного деления
# Получается (329 / 7) - 8 = 39
# Далее расчёт программный:

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
print(f'Обновлённый результат вычисления 2P: {x3_result}')

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

print(f'Итоговый результат для 2P: ({x3_result}, {y3_result})')

print(f'\n\nВычисляем 3P = 2P + P: 3P = ({x3_result}, {y3_result}) + ({x1}, {y1})')
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
# TODO: используем осмысленное слово или текст, данные ниже для практики
m_message: str = '1011101110111'

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
    temp_list.append(m_message[-3:])
    m_message = m_message[:-3]

# убираем "пустые" элементы ''
temp_list = list(filter(bool, temp_list))
# переворачиваем список
temp_list = temp_list[::-1]
print(f'Базовый список: {temp_list}')

# дополняем нулями значения списка
q_length_bits = 3 # TODO: del, дублиует значения

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
    sum_list_elements += int(elem, 2)

final_sum_list_elements = bin(sum_list_elements)[2:]
print(f'Результат сложения "кусочков" хеша: {final_sum_list_elements}')
q_bytes_peace = final_sum_list_elements[-q_length_bits:]
print(f'Берём младшие {q_length_bits} бита результата в качестве подписи, результат: {q_bytes_peace}')
print(f'Итог Шага 1 Алгоритма формирования подписи: h = h(M) = {q_bytes_peace}')

