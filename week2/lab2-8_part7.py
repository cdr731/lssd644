# Lab 2-8 Part 7 by Chris Reutz

# import requests and json libraries
import requests
import json

# API source and call
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
http_code = response.status_code

# process the return data
if http_code == 200:
    astro_data = json.dumps(response.json(),indent=4)
    print(f'{astro_data}')
# if there was an error with the API call, print out the error
else:
    print(f'HTTP error, no data processed.')
print(f'HTTP code {http_code}.')