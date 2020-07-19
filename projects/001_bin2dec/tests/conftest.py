from bin2dec import app

import pytest


@pytest.fixture()
def test_client():
    t_client = app.test_client()
    yield t_client
