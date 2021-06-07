import pytest
import math

from homework_week12.VectorClass import Vector


@pytest.fixture
def w():
    return Vector(1, 1, 1)


@pytest.fixture
def v():
    return Vector(2, 2, 2)


def test_difference():
    w = Vector(1, 1, 1)
    v = Vector(2, 2, 2)
    assert v != w


def test_add():
    w = Vector(1, 1, 1)
    v = Vector(2, 2, 2)
    assert w + v == Vector(3, 3, 3)


def test_sub():
    w = Vector(1, 1, 1)
    v = Vector(2, 2, 2)
    assert w - v == Vector(-1, -1, -1)


def test_mul():
    w = Vector(1, 1, 1)
    v = Vector(2, 2, 2)
    assert v * w == 6


def test_cross():
    w = Vector(1, 1, 1)
    v = Vector(2, 2, 2)
    assert Vector.cross(v, w) == Vector(0, 0, 0)


def test_length():
    w = Vector(1, 1, 1)
    v = Vector(2, 2, 2)
    assert Vector.length(v) == math.sqrt(12)
    assert Vector.length(w) == math.sqrt(3)


if __name__ == "__main__":
    pytest.main()
