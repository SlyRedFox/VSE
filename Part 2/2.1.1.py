# Дана переменная, в которой хранится слово из латинских букв.
# Напишите код, который выводит на экран:
# * среднюю букву, если число букв в слове нечётное;
# * две средних буквы, если число букв чётное.
#
# Пример работы программы:

# 1. word = 'test' Результат: es
# 2. word = 'testing' Результат: t

input_word: str = input('Введите слово из латинских букв (именно латиских, хотя проверок тут нет) и нажмите Enter: ')
if (len(input_word) % 2) == 0:
    first_letter_index: int = (len(input_word) // 2) - 1
    second_letter_index: int = (len(input_word) // 2) + 1
    print(f'Result: {input_word[first_letter_index:second_letter_index]}')
elif (len(input_word) % 2) == 1:
    alone_letter_index: int = (len(input_word) // 2)
    print(f'Result: {input_word[alone_letter_index]}')
else:
    print('Some strange result!')
