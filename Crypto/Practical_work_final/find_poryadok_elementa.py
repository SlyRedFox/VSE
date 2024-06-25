import math
def test(first_int, second_int):
    # result_int = 0
    result_array = []
    result_array.append(1)
    # result_array.append(first_int)
    result_text = ""
    power = 1

    
    result_int = first_int % second_int

    while result_int != 1:
        result_array.append(result_int)
        power += 1
        last_result = result_int
        result_int = (result_int * first_int) % second_int
        result_text += f"\n{first_int} ^ {power} = {last_result} * {first_int} mod{second_int} = {result_int}"

    # Первый этап, находим порядок элемента
    print("Первый этап, находим порядок элемента")
    print(result_text)
    print(f"порядок равен {power}")

    # строим группу
    print("\nCтроим группу")
    print(f"G = {{ {result_array} }}")

    # Находим порядки всех элементов
    print("\nНаходим порядки всех элементов")

    test_dict = {}
    for (i, value) in enumerate(result_array):
        if i == 0:
            print(f"O({value}) = 1")
            print()
        elif i == 1:
            print(f"O({value}) = {power}")
            print()
        else:
            print(f"O({value}) = O(x^{i}) = O({first_int}^{i}) = {power}/НОД({power}, {i}) = {power}/{math.gcd(power, i)} = {power // math.gcd(power, i)}")
 
            test123 = power // math.gcd(power, i)
            test_dict.setdefault(test123, []).append(value)

    # print(test_dict)

    # Строим подргуппы
    print("\nСтроим подгруппы")
    sorted_keys = sorted(test_dict.keys(), reverse=True)
    for key in sorted_keys:
        if key == power:
            continue

        text = f"\nH{key}"
        for el in test_dict[key]:
            text += f" = <{el}>"

        print(text)

        text_power_sub_group = f"|H{key}| = {key}"
        print(text_power_sub_group)

        min = sorted(test_dict[key])[0]
        
        text_x_sub_group = f"H{key} = {{"
        text_value_sub_group = f"H{key} = {{"

        for i in range(key):
            text_x_sub_group += f" {min}^{i}"
            text_value_sub_group += f" {pow(min, i, second_int)}"
           


        text_x_sub_group += " }"
        text_value_sub_group += " }"
        print(text_x_sub_group)
        print(text_value_sub_group)
    
test(16, 49)