from bin2dec.convert import bin2dec

import pytest


@pytest.mark.parametrize(
    ("binary", "decimal"),
    [("0", 0), ("1", 1), ("111", 7), ("1010", 10), ("100001", 33)],
)
def test_bin2dec(binary, decimal):
    assert bin2dec(binary) == decimal
