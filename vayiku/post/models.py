from django.db import models

# author
class Author(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

# category
class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title
    

# post
class Post(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    description  = models.TextField()
    category  = models.ManyToManyField("post.Category")
    time_to_read = models.CharField(max_length=255)
    featured_image = models.ImageField(upload_to="post/")
    is_draft = models.BooleanField(default=False)

    # auto field
    author = models.ForeignKey("post.Author", on_delete=models.CASCADE)
    published_date = models.DateTimeField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title