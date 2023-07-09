from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http.response import HttpResponseRedirect

# views for login
def login(request):
    #getting credentials
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check whether whether there is password and username
        if username and password:
            #check the user alread exists or not
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect("/")
        
        # if the condition not work
        context = {
            "title" : "Login",
            "error": True,
            "message" : "Invalid username or password"
        }
            
        return render(request, 'users/login.html', context)
    
    context = {
            "title" : "Login",
        }
    return render(request, 'users/login.html', context)
