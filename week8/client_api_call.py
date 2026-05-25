import requests


if __name__ == "__main__":

    URI="http://127.0.0.1:5000/jsonify"
    TOKEN="summer-sunny-days"

    print(f'Client Token: {TOKEN}')
    json_payload = {
        "auth_token":TOKEN,
        "payload":{
        "transaction_id":1234,
        "status":"active",
        "access":"administrator",
        "User":"Don"
        }    
    }
    response =requests.post(URI,json=json_payload)
    # response =requests.post(URI)
    print(F'Status code: {response.status_code}')
    print(f"*"*20)
    data=response.json()['user_data']
    print(f'{data}')
    print(f"*"*20)
    print(f'{response.json()}')


