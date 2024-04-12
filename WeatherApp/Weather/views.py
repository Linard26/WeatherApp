from django.shortcuts import render
import requests

def index(request):
    appid ='6089f83541b6dc77edf5551e12340131'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city ='London'
    res = requests.get(url.format(city)).json()
    city_info={
        'city':city,
        'temp': res["main"]["temp"],
        'icon': res['weather'][0]['icon']
    }
    context = {'info':city_info}



    return render(request, 'Weather/index.html', context)
