import pytest

import src.pyiono.math as ionomath
def test_square():
    assert ionomath.square(3.0) == 9.0
    with pytest.raises(TypeError):
        ionomath.square(3.0,2.0,1.0)

