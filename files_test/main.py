import pytest
from fibonacci import fib

# def fib(n: int) -> int:
#     return 0

@pytest.mark.parametrize("n, expected", [
    (0, 0), # Testing the base case of 0
    (1, 1), # Testing the base case of 1
    (2, 1), # Testing n=2, which is the first case of adding the two previous numbers
    (3, 2), # Testing n=3
    (4, 3), # Testing n=4
    (5, 5), # Testing n=5
    (6, 8), # Testing n=6
    (10, 55), # Testing n=10
])
def test_fibonacci(n, expected):
    assert fib(n) == expected