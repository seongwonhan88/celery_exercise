import requests

from config.settings import google_key

places = requests.get(f'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
                f'?location=-33.8670522,151.1957362'
                f'&radius=500'
                f'&types=food'
                f'&name=harbour'
                f'&key={google_key["google_api_key"]}')

if places.status_code == 200:
    print(places.text)