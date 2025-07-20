from django import forms
from .models import Actor


# A form for creating and updating Actor instances
class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor  # Connects the form to the Actor model
        fields = ['first_name', 'last_name']  # Fields to be included in the form
