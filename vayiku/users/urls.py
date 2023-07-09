from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    # loginpage
    path('login/', views.login, name='login'),
    #login
    path('logout/', views.logout, name='logout'),
    # signup
    path('signup/', views.signup, name='signup'),
]