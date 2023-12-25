from django import forms
from .models import TaskCategory
import datetime

class TaskCategoryForm(forms.ModelForm):
    class Meta:
        model= TaskCategory
        fields='__all__'
