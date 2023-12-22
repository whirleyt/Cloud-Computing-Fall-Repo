import requests

api_key = 'AIzaSyC4RJHQQgyMQXGvouZVx0h40d9qcxXqHi0'
places_api_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'


nyc_coordinates = '40.7128,-74.0060'

params = {
    'location': nyc_coordinates,
    'radius': '1000',
    'keyword': 'software company',
    'key': api_key
}


response = requests.get(places_api_url, params=params)


if response.status_code == 200:
    places_data = response.json()
    print(places_data)
else:
    print(f"Error: {response.status_code} - {response.text}")
