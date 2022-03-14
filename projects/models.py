from django.db import models
from accounts.models import UserAccount
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True, related_name='author')
    description = models.TextField()
    liked = models.ManyToManyField(UserAccount, null=True, blank=True, related_name='liked')
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    @property
    def num_likes(self):
        return self.liked.all().count()

    def __str__(self):
        return self.name