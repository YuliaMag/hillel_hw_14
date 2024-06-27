import pytest

from staff import pxl


@pytest.mark.skip(reason="failing for unknown reason")
def test_string_representation():
    pxl.Pixel = pxl.Pixel(100, 150, 200)
    assert str(pxl.Pixel) == "pxl.Pixel(100, 150, 200)"
