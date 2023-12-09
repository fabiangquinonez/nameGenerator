from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, SavedName

#identifies a form with 4 fields for registration
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


#identifies a form with 2 fields for posts meant to be shown on feeds
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['generated_name', "description"]

class SavedForm(forms.ModelForm):
    class Meta:
        model = SavedName
        fields = ['saved_name']