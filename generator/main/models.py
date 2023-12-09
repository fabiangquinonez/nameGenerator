from django.db import models
from django.contrib.auth.models import User

class Post(models.Model): #this is the model migrated to DB that stores all these fields as table columns
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if the user referenced here is deleted, the posts they had will be deleted
    generated_name = models.CharField(max_length=100, default = " ")
    description = models.TextField() #collects this from create-post decsription text field
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name + "\n" + self.description + "\n" + self.generated_name
    
class SavedName(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True) #if the user referenced here is deleted, the posts they had will be deleted
    saved_name = models.CharField(max_length = 100, null = True)

    def __str__(self):
        return self.saved_name