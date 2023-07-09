from django.shortcuts import render
from django.http.response import HttpResponse
# view for index

def index(request):
    return HttpResponse("login success fully")