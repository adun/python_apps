def test_base_route(test_client):
    url = "/"

    response = test_client.get(url)
    assert response.status_code == 200
    assert b"Converts a binary number to decimal" in response.data


def test_invalid_route(test_client):
    url = "/invalid"

    response = test_client.get(url)
    assert response.status_code == 404
    assert b"Not Found" in response.data


def test_convert_route_with_valid_binary_number(test_client):
    url = "/convert/1001"

    response = test_client.get(url)
    assert response.status_code == 200
    assert b"Bin2Dec = 9" in response.data


def test_convert_route_with_invalid_binary_number(test_client):
    url = "/convert/l00l"

    response = test_client.get(url)
    assert response.status_code == 500
    assert b"Internal Server Error" in response.data
