'''
User Story
User access admin subdomain home page and logs in
Scenarios
Success : 
          user access home page -> 200
          user logs in ( valid credentials ) and logs out -> 200
          
Errors : user provide invalid credentials -> 401 Unauthorized
         user sends a request with invalid payload -> 400 Bad Request
         
'''




url = 'http://admin.flask.com:5000/'

def test_index(test_client):
            
    response = test_client.get(url)

    assert response.status_code == 200



def test_login_and_logout_valid_credentials(test_client, init_database):
    

    response = test_client.post(url, data=dict(username='admin', password='admin'), follow_redirects=True)

    assert response.status_code == 200
    #assert b'Thanks for logging in' in response.data


    response = test_client.get(url + 'logout', follow_redirects=True)
    assert response.status_code == 200
    #assert b'Goodbye' in response.data


def test_login_invalid_credentials(test_client, init_database):


    payload = {
                'username' : 'admin',
                'password' : 'ffqasfs'
              }


    response = test_client.post(url, data=payload, follow_redirects=True)


    assert response.status_code == 200
    assert b'ERROR! Incorrect login credentials.' in response.data

