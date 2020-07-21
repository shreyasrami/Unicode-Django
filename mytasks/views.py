from django.shortcuts import render
from .binary import check_binary
from django.http import JsonResponse
# Create your views here.


def check(request,num1,num2):
    response = check_binary(num1,num2)
    return JsonResponse(response)