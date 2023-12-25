from django import forms
from .models import TaskModel
import datetime

class TaskForm(forms.ModelForm):
    class Meta:
        model= TaskModel
        fields='__all__'
        widgets={
            # 'is_completed': {'initial': False},
            'assignDate': forms.DateInput(attrs={'type': 'date'})
        }