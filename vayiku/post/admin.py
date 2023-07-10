from django.contrib import admin
from post.models import Author, Category, Post

# author admin
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "user")

admin.site.register(Author, AuthorAdmin)


# category admin
admin.site.register(Category)


#Post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "short_description")

admin.site.register(Post, PostAdmin)