import sys
from P1.myapp.sample import add
import pytest


def test_add():
    assert add(2,3) == 5


@pytest.mark.skip(reason="just wanna skip it")
def test_add_strings():
    assert add('a','b') == 'ab'


@pytest.mark.skipif(sys.version_info < (3,7), reason="will run only on versions lower than 3.7")
class TestSample:
    def test_add_num(self):
        assert add(2,3) == 5

    def test_add_strings(self):
        assert add('a', 'b') == 'ab'
