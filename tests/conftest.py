import pytest
from random import randint


@pytest.fixture()
def array1():
    length = randint(10000, 20000)
    yield [randint(0, 99999) for i in range(0, length)]
