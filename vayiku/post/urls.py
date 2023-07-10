from django.urls import path
from post import views


app_name = 'post'

urlpatterns = [
    # web
    path('create_post/', views.create_post, name='web'),
]
