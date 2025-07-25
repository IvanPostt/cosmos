import requests


def get_cliet_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_city_by_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}?lang=ru"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            return data['city']
    except:
        pass
    return 'Реутов'

def get_weather(request):
    ip = get_cliet_ip(request)
    city = get_city_by_ip(ip)
    api_key = ""
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather = {
                'city': city,
                'temp': round(data['main']['temp']),
                'description': data['weather'][0]['description'].capitalize(),
                'icon': data['weather'][0]['icon']
            }
            return weather
        else:
            return {'city': city, 'temp': '-', 'description': 'Ошибка'}
    except Exception as e:
        return {'city': city, 'temp': '-', 'description': 'Нет связи'}


