import datetime
from django import forms

from task.models import Tag, Task

class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


    class Meta:
        model = Task
        fields = ("content", "deadline", "tags")
        widgets = {
            "deadline": forms.DateInput(attrs={
                "type": "datetime-local",
                "class": "deadline"
            }),
            "content": forms.Textarea(attrs={
                "class": "content"
            }),
        }