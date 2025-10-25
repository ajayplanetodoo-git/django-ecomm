from django.shortcuts import render
from django.http import HttpResponse, request
# Create your views here.
def home_page(request):
    return HttpResponse("Hello Word")