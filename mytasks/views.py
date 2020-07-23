from django.shortcuts import render, redirect
from .binary import check_binary
from django.http import JsonResponse
import requests
from .models import Weather
# Create your views here.


def check(request, num1, num2):
    response = check_binary(num1, num2)
    return JsonResponse(response)


def weather(request):
    if request.method == 'POST':
        try:
            city = request.POST['city']
            url = 'http://api.weatherapi.com/v1/current.json?key=9fafd879443445cc9b5121427200806&q={}'.format(city)
            data = requests.get(url).json()
            city =  data['location']['name']
            country = data['location']['country']
            temperature = data['current']['temp_c']
            condition = data['current']['condition']['text']
            Weather.objects.create(city=city,country=country,temperature=temperature,condition=condition)
            context = {
                'City': city,
                'Country': country,
                'Temperature': temperature,
                'Condition': condition
                
            }
            
        except KeyError:
            context = {
                'message': 'City not found'
            }
        return render(request, 'weather.html', context)
    else:
        return render(request,'form.html')


def country_query(request):
    if request.method == 'POST':
        try:
            country = request.POST['country']
            cities = Weather.objects.filter(country__iexact=country)
            for city in cities:
                city.count += 1
                city.save()
            context = {
                'cities' : cities 
            }
        except Exception as e:
            print(e)
            context = {
                'message' : 'No country found matching the query' 
            }
        return render(request,'country_query.html',context)
    else:
        return render(request,'country_query.html')


def top3_query(request):
    cities = Weather.objects.order_by('-count')[:3]
    context = {
        'cities' : cities
    }
    return render(request,'top3_query.html',context)