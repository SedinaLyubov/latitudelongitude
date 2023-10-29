import requests

def find_uk_city(coordinates:list) -> str:
    for i in coordinates:
        url = 'https://geocode.maps.co/reverse'
        param = {
            'lat': i[0],
            'lon': i[1],
        }
        resp = requests.get(url=url, params=param).json()
        if resp['address']['country'] == 'United Kingdom':
            return resp['address']['city']


if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'