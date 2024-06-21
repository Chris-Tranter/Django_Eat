from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Preview"), (1, "Posted"))

class entry(models.Model):
    recipe = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_sharer")
    ingredients = models.TextField(max_length=150, unique=True)
    delivery = models.TextField(max_length=150, unique=True)
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    blurb = models.TextField(blank=True)
    last_edited = models.DateField(auto_now=True)