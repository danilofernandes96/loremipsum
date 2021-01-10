from django import forms
from django.forms import fields
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'startData', 'endData', 'risk', 'price', 'stakeholders']
        widgets = {
            'startData': forms.DateInput(
                attrs={'class': 'input', 'type': 'date', 'placeholder': 'Insira a data de início'}),
            'endData': forms.DateInput(
                attrs={'class': 'input', 'type': 'date', 'placeholder': 'Insira a data de término'}),
            'price': forms.NumberInput(
                attrs={'class': 'input', 'type': 'number', 'name': 'dinheiro', 'id': 'dinheiro'}),
            'stakeholders': forms.TextInput(
                attrs={'class': 'input', 'name': 'stakeholders[]'}),

        }
