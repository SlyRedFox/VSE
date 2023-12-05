# Задание 2.
# Реализуйте функцию trim_and_repeat(), которая принимает три параметра:
# строку;
# offset — число символов, на которое нужно обрезать строку слева;
# repetitions — сколько раз нужно повторить строку перед возвратом получившейся строки.
# Число символов для среза по умолчанию равно 0, а количество повторений — 1.
# Функция должна возвращать полученную строку.


def trim_and_repeat(base_string: str, offset: int = 0, repetitions: int = 1) -> str:
    """Function get some params and return repeat string"""
    return base_string[offset:] * repetitions


some_string: str = input('Input some string (required parameter): ')
cut_num = input('Input cut length (if no, just press "Enter"): ')
repeat_num = input('Input repeat number (if no, press "Enter" to): ')

if cut_num == '' and repeat_num == '':
    final_result: str = trim_and_repeat(some_string)
elif (cut_num == '') and (len(repeat_num) > 0):
    final_result: str = trim_and_repeat(some_string, repetitions=int(repeat_num))
elif (repeat_num == '') and (len(cut_num) > 0):
    final_result: str = trim_and_repeat(some_string, offset=int(cut_num))
else:
    final_result: str = trim_and_repeat(some_string, offset=int(cut_num), repetitions=int(repeat_num))

print(f'Final string: {final_result}')
