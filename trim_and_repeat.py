# Задание 2.
# Реализуйте функцию trim_and_repeat(), которая принимает три параметра:
# - строку;
# - offset — число символов, на которое нужно обрезать строку слева;
# - repetitions — сколько раз нужно повторить строку перед возвратом получившейся строки.
# Число символов для среза по умолчанию равно 0, а количество повторений — 1.
# Функция должна возвращать полученную строку.


def trim_and_repeat(base_string: str, offset: int = 0, repetitions: int = 1) -> str:
    """Function gets some params and return repeat string"""
    return base_string[offset:] * repetitions


def try_to_int(some_var: str):
    """Attempt to convert to int"""
    try:
        int(some_var)
    except Exception as error:
        print(f'Can not convert in integer variable "{some_var}"! Exit. Details: {error}')
        exit_no_logging()
    else:
        pass


# TODO: need logging
def exit_no_logging() -> exit:
    from time import sleep
    sleep(2)
    exit()


some_string: str = input('Input some string (required parameter): ')
if some_string == '':
    print('No required parameter! Exit.')
    exit_no_logging()

cut_num = input('Input cut length (if no, just press "Enter"): ')
try_to_int(cut_num)

if len(some_string) <= int(cut_num):
    print('Too big slice! Exit.')
    exit_no_logging()


repeat_num = input('Input repeat number (if no, just press "Enter"): ')
try_to_int(repeat_num)

if (int(cut_num) or int(repeat_num)) < 0:
    print('Negative parameter(s)! Exit.')
    exit_no_logging()

# TODO: need a universal solution
if cut_num == '' and repeat_num == '':
    final_result: str = trim_and_repeat(some_string)
elif (cut_num == '') and (len(repeat_num) > 0):
    final_result: str = trim_and_repeat(some_string, repetitions=int(repeat_num))
elif (repeat_num == '') and (len(cut_num) > 0):
    final_result: str = trim_and_repeat(some_string, offset=int(cut_num))
else:
    final_result: str = trim_and_repeat(some_string, offset=int(cut_num), repetitions=int(repeat_num))

print(f'\nFinal string: {final_result}')
