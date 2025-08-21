import mitchmath

def test_add():
    assert mitchmath.add(10, 10) == 20.0


def test_sub():
    assert mitchmath.sub(10, 10) == 0.0


def test_mul():
    assert mitchmath.mul(10, 10) == 100.0


def test_divi():
    assert mitchmath.divi(40, 10) == 4.0