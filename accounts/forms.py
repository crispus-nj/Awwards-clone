from xml.dom import ValidationErr
from django import forms
from .models import UserAccount

class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Password'
    }))
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class' : 'form-control',
        'placeholder': 'Repeat Password'
    }))
    class Meta:
        model = UserAccount
        fields = ['email', 'username']
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'E-Mail'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationErr("Password must match!!")
