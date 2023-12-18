from math import gcd

# ВНЕСИТЕ базовое значение множества и модуль
modul_ring = mod = 17

# ВНЕСТИТЕ значение образующего элемента
poryadok: int = 2


def obraz_elements(group: int) -> 'list':
    obr_el = list()
    for elem in range(1, group):
        poryadok_elem = group // gcd(elem, group)
        if poryadok_elem == group:
            obr_el.append(elem)
    return obr_el


obraz_elem = obraz_elements(modul_ring)
print(f'\nОбразующие элементы: {obraz_elem}\n')

final_list = [1]
for x in range(1, 100):
    print(f'{poryadok} в {x} степени {poryadok**x}')
    mod_x: int = (poryadok**x) % mod
    if mod_x == 1:
        print(f'Это по mod {mod} = {(poryadok**x) % modul_ring}, Искомая Степень: {x}')
        break
    else:
        final_list.append(mod_x)
        print(f'Это по mod {mod} = {(poryadok ** x) % modul_ring}')

print(f'\nПорядок элементов: {final_list}')
