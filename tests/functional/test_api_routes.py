

def test_index(test_client):
            
    response = test_client.get('/api/')
    print(response.status_code)
    print(response.data)
    assert response.status_code == 200
    
def test_index_users(test_client):
                 
    response = test_client.get('/api/users')
    print(response.status_code)
    print(response.data)
    assert response.status_code == 200