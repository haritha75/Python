import urllib.request
import json
from django.shortcuts import render
from django.http import HttpResponseServerError

def index(request):
    if request.method == 'POST':
        city = request.POST.get('city')

        if city:
            try:
                url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ee52facc2defac4e1cf365af45ab9f8a'.format(city)
                response = urllib.request.urlopen(url)
                data = json.loads(response.read())

                weather_data = {
                    "country_code": str(data['sys']['country']),
                    "coordinate": str(data['coord']['lon']) + ', ' + str(data['coord']['lat']),
                    "temp": str(data['main']['temp']) + ' °C',
                    "pressure": str(data['main']['pressure']),
                    "humidity": str(data['main']['humidity']),
                    'main': str(data['weather'][0]['main']),
                    'description': str(data['weather'][0]['description']),
                    'icon': data['weather'][0]['icon'],
                }
                return render(request, "main/index.html", weather_data)
            except Exception as e:
                error_message = "Error occurred while fetching weather data: {}".format(str(e))
                return HttpResponseServerError(error_message)
        else:
            return HttpResponseServerError("City name not provided.")
    else:
        return render(request, "main/index.html", {})
