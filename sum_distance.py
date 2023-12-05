# Задание 1
# Реализуйте функцию sum_distance(from, to), которая суммирует все числа от значения from до величины to включительно.
# Примечание. Если пользователь задаст первое число, которое окажется больше второго, просто поменяйте их местами.

def sum_distance(start: int, end: int) -> int:
    result: int = 0
    for num in range(start, end + 1):
        result += num
    return result


first_param: int = int(input('Input first number: '))
second_param: int = int(input('Input second number: '))

if first_param == second_param:
    from time import sleep
    print('Equal wrong params. Exit.')
    sleep(2)
    exit()

if first_param > second_param:
    print('First number > second number. Changing...')
    first_param, second_param = second_param, first_param

print(f'Final result: \t{sum_distance(first_param, second_param)}')
