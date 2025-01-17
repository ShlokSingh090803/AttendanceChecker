from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = {"first_name","last_name",'username','email','is_teacher','is_student'}
        def save(self, commit = True):
            user = super(CustomUserCreationForm, self).save(commit = False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = {'username','email'}