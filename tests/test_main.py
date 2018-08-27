def test_status_code(client):
    assert client.get('/').status_code == 200


def test_footer_content(client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/')
    assert b"Fale Conosco" in response.data
