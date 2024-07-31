from django import forms  
from .models import DreamHistory

class DreamHistoryForm(forms.ModelForm):
    class Meta:
        model = DreamHistory
        fields = ['date', 'tag', 'description']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            )
        }