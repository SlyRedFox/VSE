from math import gcd

# ВВЕДИТЕ ЗНАЧЕНИЕ ГРУППЫ G
group_g: int = 12


def nod_of_elements(group: int) -> 'tuple':
    all_elements: list = [1]
    obr_elem = list()
    for elem in range(1, group):
        print(f'x{elem} = ', end='')
        poryadok_elem = group // gcd(elem, group)
        print(poryadok_elem)
        all_elements.append(poryadok_elem)

        if poryadok_elem == group:
            obr_elem.append(elem)
    return all_elements, obr_elem


final_list, obraz_elem = nod_of_elements(group_g)

another_one_elem = list()
for x in final_list:
    if x != group_g:
        another_one_elem.append(x)

print(f'\nОбразующие элементы: {obraz_elem}')
print(f'Остальные элементы: ' + f'{set(another_one_elem)}')
