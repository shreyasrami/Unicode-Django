from django.shortcuts import render, redirect
from .binary import check_binary
from django.http import JsonResponse
import requests
from .models import Weather
from django.views.generic import TemplateView
"""
import os
from twilio.rest import Client
"""
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
            inc = Weather.objects.filter(city__iexact=city)
            hgst = inc.first()
            if hgst.count != 0:
                for i in inc:
                    i.count = hgst.count + 1
                    i.save()
            else:
                hgst.count = 1
                hgst.save()

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

        except Exception as e:
            print(e)
            context = {
                'message': 'Something went wrong'
            }
        
        finally:
            return render(request, 'weather.html', context)

        
    else:
        return render(request,'form.html')


def country_query(request):
    if request.method == 'POST':
        country = request.POST['country']
        if Weather.objects.filter(country__iexact=country):
            cities = Weather.objects.filter(country__iexact=country).order_by('city').distinct('city')
            context = {
                'cities' : cities 
            }
        else:
            context = {
                'message' : 'No country found matching the query' 
            }
        return render(request,'country_query.html',context)
    else:
        return render(request,'country_query.html')


def top3_query(request):
    cities_temp = list(Weather.objects.order_by('city').distinct('city').values())
    cities = []
    """
    account_sid = 'AC3131b2de5c0c504f06a33e6a87f6363c'
    auth_token = '69fd87f5d280cc80b1a5b3c247fcefd8'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Hello",
                        from_='+19165128656',
                        to='+91 79777 49378'
                    )

    print(message.sid)

    For Whatsapp:
    
 
    account_sid = 'AC3131b2de5c0c504f06a33e6a87f6363c' 
    auth_token = '69fd87f5d280cc80b1a5b3c247fcefd8' 
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create( 
                                from_='whatsapp:+14155238886',  
                                body='Your appointment is coming up on July 21 at 3PM',      
                                to='whatsapp:+917977749378' 
                            ) 
    
    print(message.sid)
    """

    while cities_temp:
        mn = cities_temp[0]['count']
        tp = cities_temp[0]
        for i in cities_temp:
            if i['count'] < mn:
                mn = i['count']
                tp = i
        cities.append(tp)
        cities_temp.remove(tp)
    cities = cities[::-1]
    cities = cities[:3]
    
    context = {
        'cities' : cities
    }
    return render(request,'top3_query.html',context)


class Graphs(TemplateView):
    template_name = 'graphs.html'

    def get_context_data(self,**kwargs):

        context = super().get_context_data(**kwargs)
        context['all'] = Weather.objects.order_by('city').distinct('city')
        countries = Weather.objects.order_by('country').distinct('country')
        li = []
        for country in countries:
            dc = {}
            cities = Weather.objects.filter(country=country.country).order_by('city').distinct('city')
            dc['country'] = cities
            li.append(dc)
        context['countries'] =li
        cities_temp = list(Weather.objects.order_by('city').distinct('city').values())
        cities = []

        while cities_temp:
            mn = cities_temp[0]['count']
            tp = cities_temp[0]
            for i in cities_temp:
                if i['count'] < mn:
                    mn = i['count']
                    tp = i
            cities.append(tp)
            cities_temp.remove(tp)
        cities = cities[::-1]
        cities = cities[:3]
        context['cities'] = cities
        return context



class YO:
    def hii(request):
        wthr = Weather.objects.all()
        for i in wthr:
            print(i)