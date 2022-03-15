from django import forms
from .models import UserAccount

class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs= {
        'class' : 'form-control form-input',
        'placeholder' : 'Password'
    }))
    confirm_password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={
        'class' : 'form-control form-input',
        'placeholder' : 'Repeat Password'
    }))
    class Meta:
        model = UserAccount
        fields = ['email', 'username']
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['email'].widget.attrs['placeholder'] = 'E-Mail'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password must match!!")
    
class ProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs= {
        'class' : 'form-control',
    }))
    email = forms.EmailField(max_length=200, widget=forms.TextInput(attrs= {
        'class' : 'form-control',
    }))
    bio = forms.CharField(max_length=200, widget=forms.Textarea(attrs= {
        'class' : 'form-control',
        'cols' : 200,
        'rows': 3,
        'style': 'width: 100%'
    }))
    avatar = forms.ImageField(widget=forms.ClearableFileInput(attrs= {
        'class' : 'form-control',
    }))
    class Meta:
        model = UserAccount
        fields = ['username', 'bio', 'email' ,'avatar']
