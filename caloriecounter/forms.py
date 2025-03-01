from django import forms
from django.forms import ModelForm
from .models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model: Profile
        fields = ('your_goal', 'start_weight', 'goal_weight', 'week_goal', 'calorie_goal', 'activity')
        widgets = {
            'your_goal': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 450px;'}),
        }