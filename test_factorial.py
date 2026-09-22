from factorial import factorial

def test_factorial():
    assert factorial(1)==1

def test_factorial2():
    assert factorial(5) == 120


def test_negative_factorial3():
    assert factorial(2) == 2