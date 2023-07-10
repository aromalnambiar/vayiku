from django import forms
from post.models import Post

class PostForm(forms.ModelForm):

    tags = forms.CharField(label="Tags (Comma separated)")
  
    class Meta:
        model = Post
        exclude = ("author", "published_date", "is_deleted", "category")