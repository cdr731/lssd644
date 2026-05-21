import requests

if __name__ == "__main__":

  URI="http://127.0.0.1:5001/jsonify"
  TOKEN="summer-sunny-days"

  print(f'Client Token: {TOKEN}')
  #Add code here
  json_payload={
      "auth_token":TOKEN,
      "payload":{
          "transaction_id":1234,
          "status":"active",
          "access":"Admin",
          "user":"Chris"
      }
  }
  
  try:
      response =requests.post(URI,json=json_payload)
      print(f"Response status: {response.status_code}")
      print(f'API response: {response.json()}')

  except requests.exceptions.ConnectionError:
      print(f"Flask running on 5001?")
