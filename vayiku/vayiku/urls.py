
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls for app users
    path('users/', include("users.urls", namespace="users")),
    #root url aka web module
    path('', include("web.urls", namespace="web"))
]
