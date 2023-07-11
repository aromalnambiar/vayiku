import datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from post.form import PostForm
from post.models import Author

@login_required(login_url="/users/login")
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            if not Author.objects.filter(user=request.user).exists():
                author = Author.objects.create(name=request.user.username, user=request.user)
            else:
                author = request.author.author

            instance = form.save(commit=False)
            instance.published_date = datetime.date.today()
            instance.author = author
            instance.save()
            
    else:   
        data = {
            "title" : "aromal",
            "description" : "aromal",
            "short_description" : "aromal",
            "time_to_read" : "8 min",
            "tags" : "technology, programming, coding"
        } 
        form = PostForm(initial=data)
        context = {
            "title": "create post",
            "form" : form,
        }

        return render(request, "post/create_post.html", context)
