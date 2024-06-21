from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def its_breakfast(request):
    return HttpResponse("Breakfast menus!")