from django.shortcuts import render
import requests
from .forms import *
from .models import *
from django.conf import settings


def weather_view(request):
    error = ""
    weather = ""
    key = settings.WEATHER_API_KEY
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            url = (f"http://api.openweathermap.org/data/2.5/weather"
                   f"?q={city}&appid={key}&units=metric&lang=ru")
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather = Weather.objects.create(
                    city=city,
                    temperature=data['main']['temp'],
                    description=data['weather'][0]['description'],
                    humidity=data['main']['humidity'],
                    speed=data['wind']['speed'],
                    pressure=data['main']['pressure']
                )
            else:
                error = "Город не найден"
    form = CityForm()

    return render(request, 'weather.html', {'form': form, 'weather': weather, 'error': error})


def records(request):
    records = Weather.objects.all().order_by('-created_at')
    return render(request, 'records.html', {'records': records})