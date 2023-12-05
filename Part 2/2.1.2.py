queries: list = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

znacheniya: list = list()
for element in queries:
    words_count = len(element.split())
    znacheniya.append(words_count)

final_counts: dict = {number: znacheniya.count(number) for number in set(znacheniya)}
vsego_elementov: int = len(znacheniya)
for key, value in final_counts.items():
    print(f'Поисковых запросов, содержащих {key} слов(а): {(value*100)/vsego_elementov:.2f}%')