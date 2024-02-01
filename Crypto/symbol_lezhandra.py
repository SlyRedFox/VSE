# Символ Лежандра + нахождение простых множителей.

# Внимание! Сложно привести к единому коду!
# Много свойств, совпадение с которыми нужно проверять.
# Потрачу больше времени на написание кода, чем работая по конспекту. Поэтому тут только пример раскладывания на простые числа.
# Далее следуем конспекту.

# Являетсая ли число квадратичным вычетом или невычетом по модулю p > 1
# Задача: всё в скобках, в числителе 426, в знаменателе 557
# (426
#  ---
#  557)

chislitel_start: int = 426
znamenatel_start: int = 557

print('\nРаскладываем на простые числа "числитель"')
simple_chisla: list = []
delitel: int = 2

while delitel <= chislitel_start:
    if chislitel_start % delitel == 0:
        simple_chisla.append(delitel)
        chislitel_start = chislitel_start // delitel
    else:
        delitel += 1

print(*simple_chisla)

print(f'Можем представить исходный пример как {len(simple_chisla)} разных дроби (записываем именно как дробь, пример на стр. 39 конспекта)')
count: int = 1
for elem in simple_chisla:
    print(f'Номер {count}: {elem} / {znamenatel_start}')
    count += 1
