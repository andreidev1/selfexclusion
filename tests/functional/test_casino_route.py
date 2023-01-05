'''
User Story
User access /casino and will register using HTML form
Scenarios
Success -> returns 201
Fail -> incomplete data /  returns 400 BAD REQUEST 
     -> returns 405 invalid HTTP method

'''
import datetime
import jwt

def test_index(test_client):

    response = test_client.get('/register_casino')

    assert response.status_code == 200

# Stub Test
def test_register_casino_form(test_client, init_database):

    auth_key = jwt.encode({'some' : 'payload'}, 'secret', algorithm='HS256')

    payload = {
                'name' : 'Las Vegas',
                'email' : 'admin@lasvegas.com',
                'timestamp' : datetime.datetime.utcnow(),
                'auth_key' : auth_key
            }

    

    response = test_client.post('/register_casino', data=payload, follow_redirects=True)

    assert response.status_code == 201

def test_register_casino_form_invalid_http_method(test_client):

    payload = {
        'name' : 'Don Cash'
    }

    response = test_client.put('/register_casino', data=payload)


    assert response.status_code == 405