import pytest
from dp import *


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (4, [0, 1, 1, 2, 1]),
        (6, [0, 1, 1, 2, 1, 2, 2]),
    ),
)
def test_countBits(input, expected):
    assert countBits(input) == expected


@pytest.fixture
def pascal_triangle():
    tri = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    return tri


def test_generate_pascal_triangle(pascal_triangle):
    assert generate_pascal_triangle(5) == pascal_triangle


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (1, 1),
        (2, 1),
        (5, 5),
        (6, 8),
        (10, 55),
    ),
)
def test_fib_and_fib_rec(input, expected):
    assert fib(input) == fib_rec(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (1, 1),
        (2, 1),
        (5, 7),
        (6, 13),
        (10, 149),
    ),
)
def test_tribonacci(input, expected):
    assert tribonacci(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ([1, 2, 3, 4, 5, 6], 5),
        ([2, 7, 1, 2, 1, 5], 5),
        ([8, 9, 5, 3, 5, 6, 7, 1], 4),
    ),
)
def test_maxProfit(input, expected):
    assert maxProfit(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (5, 8),
        (0, 0),
        (6, 13),
    ),
)
def test_climbStairs(input, expected):
    assert climbStairs(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        ([1, 1, 1, 1, 1, 1, 1], 3),
        ([5, 0, 1, 2, 1, 4], 2),
        ([2, 20, 1, 30, 24, 1], 27),
    ),
)
def test_min_cost_climbing_stairs(input, expected):
    assert minCostClimbingStairs(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    (
        (1, 1),
        (2, 1),
        (4, 2),
        (7, 3),
    ),
)
def test_get_maximum_generated(input, expected):
    assert getMaximumGenerated(input) == expected
