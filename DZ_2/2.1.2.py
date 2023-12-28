# Есть список юношей и девушек.
# Выдвигаем гипотезу: лучшие рекомендации получатся, если просто отсортировать имена по алфавиту и познакомить людей с
# одинаковыми индексами после сортировки. Но вы не будете никого знакомить, если кто-то может остаться без пары.

# Пример 1
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
# Результат:
# Идеальные пары:
# Alex и Emma
# Arthur и Kate
# John и Kira
# Peter и Liza
# Richard и Trisha

# Пример 2
# boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael'] Peter Alex John Arthur Richard Michael
# girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']               Kate Liza Kira Emma Trisha
# Результат: Внимание, кто-то может остаться без пары!

boys: list = [boy_name for boy_name in input('Input boys names (separated by a space) and press "Enter": ').split()]
boys = sorted(boys)
girls: list = [girl_name for girl_name in input('Input girls names (separated by a space) and press "Enter": ').split()]
girls = sorted(girls)

if len(boys) > len(girls):
    print('\nВнимание, кто-то может остаться без пары! Завершение программы.')
    exit()
else:
    print('Идеальные пары:')
    for number in range(len(boys)):
        print(f'{boys[number]} и {girls[number]}')
