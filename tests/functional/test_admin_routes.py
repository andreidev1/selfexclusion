def test_index(test_client):
            
    response = test_client.get('http://admin.flask.com:5000/')
    print(response.status_code)
    print(response.data)
    assert response.status_code == 200