from django import forms
from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'grade', 'teacher', 'schedule', 'academic_year', 'max_students', 'description', 'subjects']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter group name',
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'grade': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'teacher': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'schedule': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'academic_year': forms.TextInput(attrs={
                'placeholder': 'e.g 2023-2024',
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'max_students': forms.NumberInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter description',
                'class': 'w-full px-3 py-2 border rounded-md'
            }),
            'subjects': forms.SelectMultiple(attrs={
                'class': 'w-full px-3 py-2 border rounded-md'
            })
        }