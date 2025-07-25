from .weather import get_weather

def weather_processor(request):
    return {'weather': get_weather(request)}
