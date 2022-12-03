'''
User Story
User posts data using route /submit-data
Scenarios
1) Success -> returns 201
2) Errors -> Method not allowed -> 405
         -> Bad request ( not validating all data) -> 400
'''

def test_index(test_client):
            
    response = test_client.get('/')

    assert response.status_code == 200

def test_submit_form_success(test_client):
    
    response = test_client.post('/submit-data')

    assert response.status_code == 201

def test_submit_form_fail_400(test_client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/submit-data' page is requested (POST)
    THEN expect not completed form to be submitted
    '''
    payload = {
                'name' : 'Andrew',
                'cnp' : '50000000',
                'number_phone' : '07541241'
              }


    response = test_client.post('/submit-data', json=payload)

    assert response.status_code == 400

def test_submit_form_fail_405(test_client):
    '''
    GIVEN a Flask application configured for testing
    WHEN the '/submit-data' page is requested (GET)
    THEN expect method not allowed
    '''
    
    response = test_client.get('/submit-data')

    assert response.status_code == 405

