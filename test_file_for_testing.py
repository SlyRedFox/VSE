from testing import multiplication_magic as mm_func


def result_test(a: int, b: int):
    res: int = mm_func(a, b)

    # testing
    test_res = a * b
    assert res == test_res


def type_test(a: int, b: int):
    res: int = mm_func(a, b)
    type_a = type(a)
    type_b = type(b)
    # testing
    number_1: int = 10
    number_2: int = 20
    assert type(number_1) is type_a
    assert type(number_2) is type_b
    return res


# run test-functions
result_test(1, 2)
result_test(5, 7)

type_test(9, 10)
type_test(15, 17)
