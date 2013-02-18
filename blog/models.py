from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from taggit.managers import TaggableManager

class Post(models.Model):
    title  = models.CharField(max_length=100)
    slug   = models.SlugField()
    text   = models.TextField()
    author = models.ForeignKey(User) # CurrentUserField?
    date   = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    tags   = TaggableManager()

class PostForm(ModelForm):
    class Meta:
        model = Post
