from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            "password" :  forms.widgets.PasswordInput(attrs={
            "placeholder" : "Password",
            }),

            "first_name" : forms.widgets.TextInput(attrs={
            "placeholder" : "First Name",
            "class": "hello"
            }),

            "last_name" : forms.widgets.TextInput(attrs={ 
                "placeholder" : "Last Name",
            }),

            "username" : forms.widgets.TextInput(attrs={ 
                "placeholder" : "Username",
            }),

            "email" : forms.widgets.EmailInput(attrs={ 
                "placeholder" : "Email",
            })
        }