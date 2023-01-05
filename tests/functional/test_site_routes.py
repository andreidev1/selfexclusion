'''
User Story
User posts data using route /
Scenarios
1) Success -> returns 201
2) Errors -> Method not allowed -> 405
          -> Bad request ( not validating all data) -> 400
'''

import datetime
import pytest

def test_index(test_client):

        
    response = test_client.get('/')

    assert response.status_code == 200

def test_submit_form_success(test_client, init_database):
    pytest.skip()
    image = 'kyc.png'
    #files = {'selfie_kyc' : open('kyc.png', 'rb')}
    headers = {'Content-Type' : 'multipart/form-data'}

    data = {'name': 'Andrew', 
            'cnp': '1234567890123', 
            'number_phone': '0785454541',
            'email_address': 'myusertest@gmail.com', 
            'selfie_kyc': image, 
            'verified': False, 
            'selected_casinos': 'Las Vegas', 
            'timestamp': str(datetime.datetime.utcnow()), 
            'period': 'Permanently'}
    files = {'selfie_kyc' : open(image, 'rb')}
    response = test_client.post('/', headers=headers, data=data, files=files)



    assert response.status_code == 201


def test_submit_form_fail_405(test_client, init_database):


    response = test_client.put('/', data=dict(name='Andrew', 
                                               cnp='1234567890123', 
                                               number_phone='0785454541',
                                               email_address='myusertest@gmail.com',
                                               selfie_kyc=None,
                                               verified=False,
                                               selected_casinos='Las Vegas',
                                               timestamp=str(datetime.datetime.utcnow),
                                               period='Permanently'
                                               ))



    assert response.status_code == 405
