from django import forms
from .models import Plan


class PlanForm(forms.ModelForm):
    """Form for the Workout model"""

    class Meta:
        model = Plan
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email_address',
            'your_goal',
            'plan_type',
        )
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'your_goal': forms.TextInput(attrs={'class': 'form-control'}),
            'plan_type': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
