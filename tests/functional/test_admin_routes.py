'''
User Story
User access admin subdomain homepage and logs in
Scenarios
Success : user access homepage and logs in -> 200
Errors : user provide invalid credentials -> 401 Unauthorized
         user sends a request with invalid payload -> 400 Bad Request
         
'''



def test_index(test_client):
            
    response = test_client.get('http://admin.flask.com:5000/')

    print(response.status_code)
    print(response.data)

    assert response.status_code == 200

def test_login_valid_credentials(test_client):

    response = test_client.post('http://admin.flask.com:5000/')

    payload = {
                'username' : 'Admin',
                'password' : '123456'
              }


    assert response.status_code == 200


def test_login_invalid_credentials(test_client):

    response = test_client.post('http://admin.flask.com:5000/')

    payload = {
                'username' : 'Admin',
                'password' : '123456!*@(#DSAHDJASHD'
              }


    assert response.status_code == 401

def test_login_invalid_payload(test_client):
    response = test_client.post('http://admin.flask.com:5000/')

    payload = {
                'username' : 'Admin',
                'mypassword' : '123456!*@(#DSAHDJASHD'
              }


    assert response.status_code == 400