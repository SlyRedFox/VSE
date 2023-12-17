from math import gcd

# Базовое значение множества
modul_ring: int = 17

# Значение образующего элемента
poryadok: int = 8


def obraz_elements(group: int) -> 'lists':
    obr_el = list()
    for elem in range(1, group):
        poryadok_elem = group // gcd(elem, group)
        if poryadok_elem == group:
            obr_el.append(elem)
    return obr_el


obraz_elem = obraz_elements(modul_ring)
print(f'\nОбразующие элементы: {obraz_elem}\n')

# for x in range(1, 100):
#     print(f'{poryadok} в {x} степени {poryadok**x}')
#     mod_x: int = (poryadok**x) % 15
#     if mod_x == 1:
#         print(f'Это по mod 15 = {(poryadok**x) % modul_ring}, искомая степень {x}')
#         break
#     else:
#         print(f'Это по mod 15 = {(poryadok ** x) % modul_ring}')
