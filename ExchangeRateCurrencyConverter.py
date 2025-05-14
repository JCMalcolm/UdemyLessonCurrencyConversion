import requests
import os
import json

base_url = 'https://api.exchangeratesapi.io'

api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API key not set!")


date = input('Please enter the date in the format of "YYYY-MM-DD": ')
# project asks for base, but changing base is limited to paid accounts and I am not paying for this API today
curr = input('What currency do you with to convert EUR to? And please use the 3 letter currency code: ')
quan = float(input('How much EUR do you want to convert: '))

url = base_url + '/' + date
params = {'access_key': api_key, 'symbols': curr}

response = requests.get(url, params=params)

if(response.ok is False):
    print(f'\nError {response.status_code}')
    print(response.json().get('error', 'No error message returned'))
else:
    data = response.json()
    try:
        rate = data['rates'][curr]
        result = round(quan*rate, 2)
        print(f'\n{(quan)} EUR is equal to {result} {curr}, based upon exchange rates on {data["date"]}')
    except KeyError:
        print("Currency code not found in response. Double-check the currency symbol.")
        print("Response content:", data)

"""

Results obtained with local API key:

Please enter the date in the format of "YYYY-MM-DD": 2003-05-02
What currency do you with to convert EUR to? And please use the 3 letter currency code: CAD
How much EUR do you want to convert: 432

432.0 EUR is equal to 687.96 CAD, based upon exchange rates on 2003-05-02

"""