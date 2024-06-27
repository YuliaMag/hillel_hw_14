from staff import pxl


def test_addition():
    pxl.pixel1 = pxl.Pixel(100, 150, 200)
    pxl.pixel2 = pxl.Pixel(50, 75, 100)

    result = pxl.pixel1 + pxl.pixel2
    assert result.red == 150
    assert result.green == 225
    assert result.blue == 255
