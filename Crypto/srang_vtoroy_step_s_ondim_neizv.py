# Сравнение второй степени с одним неизвестным: x**2 ≡ a mod p
# Здесь минимальный набор, всё вычисляется на основе предыдущих задач вручную
# Задача: x**2 ≡ 2 mod 113

# Вносим базовые значениея
a_start: int = 347
p_start: int = 761

print(f'\nШаг 1. \nВычисляем вручную символ Лежандра для ({a_start}/{p_start}). Если необходимо раскладывать число на простые множители используем скрипт symbol_lezhandra.py')
print('В нашем случае работали по свойству 1, получилась 1, значит, корни есть и можно продолжать вычисления')

print('\nШаг 2. Выбираем целое b, где (b/p) = -1 (стр. 38 конспекта). Расчёт на стр. 44. Итог: b = 3')

print(f'\nШаг 3. Представить {p_start} - 1 = 2**s * t, где t - нечётное')
stepen_dvoyki: int = 1
t_num: int = (p_start - 1) // 2
while t_num % 2 == 0:
    stepen_dvoyki += 1
    t_num = t_num // 2

print(f'Степень двойки, s = {stepen_dvoyki}, число t = {t_num}')

print(f'\nШаг 4. Находим РАЕ для {a_start}**-1 % {p_start}. Используем скрипт 4_rae.py \nРезультат для нашего примера (приводим обязательно к положительному): 57')

print('\nШаг 5. Вычисление по формуле C0 и г, вручную, не сложно.')

print('\nШаг 6. Вносим нужные данные и вычисляем по циклу: i = 1 ... s-1 \n Если получается большое значение,'
      ' просто вычти из него значение mod, например, при i = 2 будет 112, а 112 - 113 = -1 '
      '\n ВНИМАТЕЛЬНО СЛЕДИМ, обновились ли параметры! После шага 2 r уже будет 62')
i = 2
r = 44
a = 318
s = 3
di = ((r**2 * a)**2**(s-i-1)) % p_start
print(f'\nResult is: d{i} = {di}')