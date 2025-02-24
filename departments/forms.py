from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'head', 'description', 'location', 'contact_email', 'contact_phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Add department name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'head': forms.TextInput(attrs={
                'placeholder': 'Department head name',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter department description',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'Enter department location',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'contact_email': forms.EmailInput(attrs={
                'placeholder': 'Enter contact email',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            }),
            'contact_phone': forms.TextInput(attrs={
                'placeholder': 'Enter contact phone',
                'class': 'w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'
            })
        }