from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http.response import HttpResponseRedirect

from users.forms import UserForm
from main.function import get_error
from post.models import Author

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


# view for login
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect("/")

# view for the signup
def signup(request):
    # checking the data in the form
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # creating user
            instance = form.save(commit=False)
            User.objects.create_user(
                first_name=instance.first_name,
                last_name=instance.last_name,
                username=instance.username,
                email=instance.email,
                password=instance.password,
            )

            Author.objects.create(name=instance.first_name, user=user)
            
            # login the created user
            user = authenticate(request=request, username=instance.username, password=instance.password)
            auth_login(request, user)


            return HttpResponseRedirect("/")
            
        else:
            message = get_error(form)

            form = UserForm()
            context = {
                "title" : "Sign Up",
                "form" : form,
                "error" : True,
                "message" : message,
            }
            return render(request, "users/signup.html" , context)

    else:
        form = UserForm()
        context = {
            "title" : "Sign Up",
            "form" : form
        }
        return render(request, "users/signup.html" , context)