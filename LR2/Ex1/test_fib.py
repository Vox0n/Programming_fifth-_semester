def test_fib_1():
    gen = my_genn()
    # Для корутины нужно сначала отправить значение, затем получить результат
    assert gen.send(3) == [0, 1, 1], "Тривиальный случай n = 3, список [0, 1, 1]"

def test_fib_2():
    gen = my_genn()
    assert gen.send(5) == [0, 1, 1, 2, 3], "Пять первых членов рядов"

def test_fib_3():
    gen = my_genn()
    assert gen.send(8) == [0, 1, 1, 2, 3, 5, 8, 13], "Восемь первых членов рядов"

def test_fib_4():
    gen = my_genn()
    assert gen.send(1) == [0], "Один первый член ряда"
