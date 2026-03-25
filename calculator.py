from calculator import add

def add(a: float, b: float) -> float: return a + b

def sub(a: float, b: float) -> float: return a + b

def mul(a: float, b: float) -> float: return a * b

def div(a: float, b: float) -> float: return a/b

def test_add():
    assert add (2, 3) == 5