#En esta asignacion escribiras un programa en python que analizar por una locacion, contactar un servicio web y recibir JSON por el servicio web y analizar esa data, y devolver el primer lugar_id desde un JSON. Un place_id es un identificador textuar que unicamente identifica por un lugar como en google maps 

import urllib.request
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = "https://py4e-data.dr-chuck.net/json?"
else: 
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True: 
    address= input("Enter location: ")
    if len(address) < 1:
        break

    params = dict()
    params['address'] = address
    if api_key is not False: params['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(params)


    print('Retrieving', url)
    file = urllib.request.urlopen(url, context=None)
    data = file.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    

    location_id = js['results'][0]['place_id']
    print('Place id ',location_id)