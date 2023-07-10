from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login")
def create_post(request):
    context = {
        "title": "create post",
    }

    return render(request, "post/create_post.html", context)
