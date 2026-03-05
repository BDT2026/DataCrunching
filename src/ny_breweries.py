import requests
import json

url = "https://api.openbrewerydb.org/v1/breweries?by_city=New York"

payload = {}
headers = {
}

response = requests.request("GET", url, headers=headers, data=payload)

if response.status_code == 200:
    json_data = json.loads(response.text)
    print(type(json_data[0])  )
else:
    raise ValueError("Brewery API returned a non-200 status code")
