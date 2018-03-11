from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add=True)
    # add thumbnail later
    thumb = models.ImageField(default='defualt.jpg', blank=True)
    # add author late
    author = models.ForeignKey(User,default=None)

    def snippet(self):
        return self.body[:70] + '....' if len(self.body) > 70 else self.body[:70]

    def __str__(self):
        return self.title
