from django.shortcuts import render, redirect
from .binary import check_binary
from django.http import JsonResponse
import requests
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
            context = {
                'City': data['location']['name'],
                'Temperature': data['current']['temp_c'],
                'Weather': data['current']['condition']['text'],
                'Country': data['location']['country'],
            }
            
        except KeyError:
            context = {
                'message': 'City not found'
            }
        return render(request, 'weather.html', context)
    else:
        return render(request,'form.html')
