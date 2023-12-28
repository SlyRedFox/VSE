# Instruction
# Переведите содержимое файла purchase_log.txt в словарь purchases вида:
# {'1840e0b9d4': 'Продукты', ...}
# Пример работы программы при выводе первых двух элементов словаря purchases:
# 1840e0b9d4 ‘Продукты‘
# 4e4f90fcfb  ‘Электроника‘

# we have a file purchase_log_test.txt in base directory with only five strings for testing
# FILE_WAY_NAME: str = './purchase_log_test.txt'
FILE_WAY_NAME: str = './purchase_log.txt'
purchases = dict()
supportive_dict = dict()

with open(FILE_WAY_NAME, 'r', encoding='utf-8') as read_file:
    first_string = read_file.readline()
    second_string = read_file.readline()

base_element: list = second_string.split('"')
purchases[base_element[7]] = base_element[3]


with open(FILE_WAY_NAME, 'r', encoding='utf-8') as read_file:
    for line in read_file:
        elements: list = line.split('"')
        supportive_dict[elements[3]] = elements[7]

# delete first element of dict (see Instruction above)
strange_key: str = 'user_id'
if strange_key in supportive_dict:
    del supportive_dict[strange_key]

another_strange_key: str = 'Продукты'
if another_strange_key in supportive_dict:
    del supportive_dict[another_strange_key]

purchases.update(supportive_dict)
# if you REALLY need this... uncomment next line
# print(f'\nFinal: {purchases}')
