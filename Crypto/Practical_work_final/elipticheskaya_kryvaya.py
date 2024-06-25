def check1(a,b,p):
    print('Шаг 1')
    print("Проверка глаткости: -4*a^3 - 27*b^2 ≠ 0")
    check = -4*(a**3)-27*b
    print(f"-4*({a}^3) - 27*({b}^2) = -4*({a**3}) - 27*({b**2}) = {check}mod p = {check%p}  ")
    if check != 0:
        print("Все ок ")
    else:
        print("Не прошли проверку гладкости")
    print()
    print()

def check2(a,b,p):
    print('Шаг 2')
    print(f'Построить таблицу конечного поля (F{p})')
    f1 = "{" + ", ".join([str(i) for i in range(0, p)]) + "}"
    data_set = "{" + ", ±".join([str(i) for i in range(0, p//2 + 1)]) + "}"
    print(f'F{p} = {f1} = {data_set}')
    print()
    print()
    print()


def check3(data_set,p):
    print(f"Составим таблицу квадратов")
    data_set = [i for i in range(0, p//2 + 1)]
    for i in data_set:
        if (i**2)%p == i**2:
            print(f"(±{i})^2 = {i**2}")
        else:
            print(f"(±{i})^2 = {i**2} = {i**2 % p}")
    print()
    print()
    print()
def check_m(a,b,p):
    while True:
        data = {}
        data["a"] = a
        data["b"] = b
        data["p"] = p
        p = data["p"]
        a = data["a"]
        b = data["b"]
        num = 1
        data_x_and_y = set()
        F_m_squared_mod = {(y**2) % p: y for y in tuple(range(0, int(p/2)))}
        print()
        print(f"y^{2} = x^{3} + ({a})*x + ({b}) ")
        for x in tuple(range(int(-p/2), int(p/2)+1)):
            y = (x**3 + a * x + b) % p #
            print(f"x = {x}; y^2 = {x}^3 + {a} * {x} + {b} = {x%p} + {(a*x)%p} + {b%p} = {x**3 + a*x + b} = {(x**3 + a*x + b)%p}")
            if y == 0:
                data_x_and_y.add((x, y))
                print(f"    P{num} = ({x}, {y})")
                num += 1
            elif y in F_m_squared_mod:
                print(f"    P{num} = ({x}, {-F_m_squared_mod[y]})")
                num += 1
                print(f"    P{num} = ({x}, {F_m_squared_mod[y]})")
                num += 1
                data_x_and_y.add((x, -F_m_squared_mod[y]))
                data_x_and_y.add((x, F_m_squared_mod[y]))
            else:
                print(f"    ----------")
            print()
        return data


def main():
    a = 8
    b = 5
    p =17
    print(f"Построить и исследовать группу точке элептической кривой Е{a},{b} (F{p})")
    check1(a,b,p)
    data_set = check2(a, b, p)
    check3(data_set,p)
    data = check_m(a,b,p)

main()