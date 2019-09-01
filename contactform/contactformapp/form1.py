from django import forms
class EmpForm(forms.Form):
    name=forms.CharField(
        label="enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    email=forms.EmailField(
        label='enter your email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder':'your email id'
            }
        )
    )
    salary = forms.IntegerField(
        label="enter your salary",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your salary'
            }
        )
    )
    location = forms.CharField(
        label="enter your location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your location'
            }
        )
    )