from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if the user referenced here is deleted, the posts they had will be deleted
    name = models.CharField(max_length=200, default="hello")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name + "\n" + self.description
    
