import pytest
from contextlib import nullcontext as does_not_raise
from src.main import prakt

@pytest.mark.parametrize(
    "one , two , rez",
    [
    (1 , 2 , 3),
    (-1,-3,-4),
    (1.0 , 2.5 , 3.5),
    ]
)
def test_add(one , two ,rez):
    assert prakt().add(one,two)==rez

def test_divide1():
    assert prakt().divide(2 , 1) == 2

def test_divide2():
    with pytest.raises(ValueError):
        assert prakt().divide(2, 0) == ValueError

@pytest.mark.parametrize(
        "stroka , result",
        [
            ("Толик" , False),
            ("А роза упала на лапу Азора", True),
        ]
)
def test_is_palindrome(stroka , result):
    assert prakt().is_palindrome(stroka) == result        
