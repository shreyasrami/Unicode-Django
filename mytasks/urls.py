from django.urls import path
from . import views


urlpatterns=[
    
    path('<int:num1>/<int:num2>/',views.check,name='check_binary_view'),
    path('',views.weather,name='weather'),
    path('country-query',views.country_query,name='country_query'),
    path('top3-query',views.top3_query,name='top3_query'),
    
]
