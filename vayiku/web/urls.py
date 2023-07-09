from django.urls import path
from web import views


app_name = 'web'

urlpatterns = [
    # web
    path('', views.index, name='web'),
]
