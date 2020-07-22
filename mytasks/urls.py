from django.urls import path
from . import views


urlpatterns=[
    
    path('',views.weather,name='weather'),
    path('<int:num1>/<int:num2>/',views.check,name='check_binary_view'),
    
]
