from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import *

class ProfileMF(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','timezone','profile_image']

class UserMF(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']
        help_texts={'username':''}

class TaskMF(forms.ModelForm):
    class Meta:
        model = TaskTable
        fields = ['title', 'category', 'description', 'priority', 'status', 'due_date']
        widgets = {
            'due_date': forms.DateTimeInput(
                attrs={'type': 'datetime-local'},
                format='%Y-%m-%dT%H:%M'
            ),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['category'].queryset = Category.objects.filter(user=user)

        self.fields['due_date'].input_formats = ['%Y-%m-%dT%H:%M']


class CategoryMF(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


