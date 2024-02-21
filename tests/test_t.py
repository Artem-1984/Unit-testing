from menu import Translation
import pytest


def test_get_translation():
    assert Translation(10).get_num() == 10


@pytest.mark.parametrize("number, error", [('sdf', TypeError),
                                           (0, TypeError), ])
def test_translate_8(number, error):
    with pytest.raises(error):
        Translation(number).translate_num_8x(oct(number))


@pytest.mark.parametrize("number, error", [(12, NameError)])
def test_translate_2(number, error):
    with pytest.raises(error):
        Translation(number).translate_num_2x(hex(numbers))


@pytest.mark.parametrize("number, error", [(10.5, TypeError)])
def test_translate_16(number, error):
    with pytest.raises(error):
        Translation(number).translate_num_16x(bin(number))
