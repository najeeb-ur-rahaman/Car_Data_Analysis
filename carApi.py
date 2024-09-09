import requests
from dotenv import load_dotenv
import os

base_url = "https://carapi.app/api"

def configure():
    load_dotenv()

def get_data(id):
    try:
        print("Getting car data for ID:", id)
        url = f"{base_url}/trims/{str(id)}"
        payload = {}
        headers = {
        'Authorization': 'Bearer ' + os.getenv('token')
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        yield response.json()
        
    except Exception as e:
        print(e)
        print(url)

def get_id(make, year):
    try:
        print("Getting trims for make:", make)
        url = f"{base_url}/trims?year={year}&make={make}"
        payload = {}
        headers = {
        'Authorization': 'Bearer ' + os.getenv('token')
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        data = response.json()
        if data is not None:
            for key in data['data']:
                # Yield all the car data from get_data
                yield from get_data(key['id'])

    except Exception as e:
        print(e)
        print(data)
        print(url)

    
def get_makes(year):
    configure()
    try:
        print("Getting makes for year:", year)
        url = f"{base_url}/makes?year={year}"
        payload = {}
        headers = {
        'Authorization': 'Bearer ' + os.getenv('token')
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        data = response.json()
        if data is not None:
            for pair in data['data']:
                # Yield all data from get_id
                yield from get_id(pair['name'], year)

    except Exception as e:
        print(e)
        print(data)
