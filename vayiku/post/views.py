from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from post.form import PostForm

@login_required(login_url="/users/login")
def create_post(request):
    if request.method == "POST":
        pass
    else:    
        form = PostForm()
        context = {
            "title": "create post",
            "form" : form,
        }

        return render(request, "post/create_post.html", context)
