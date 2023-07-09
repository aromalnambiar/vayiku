from django.shortcuts import render
from django.http.response import HttpResponse


# view for index
def index(request):
    context = {
        'title': 'Vayiku',
    }
    return render(request, 'web/index.html' , context)