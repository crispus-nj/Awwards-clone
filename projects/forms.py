from django import forms
from .models import Project

class PostProjectForm(forms.ModelForm):
    description = forms.CharField( widget = forms.Textarea(attrs={
        'class' : 'form-control',
        'placeholder': 'Project Description...',
        'cols': 200,
        'rows': 3,
        'style': 'width: 100%'
    }))
    class Meta:
        model = Project
        fields = ['name', 'project_link', 'image']

    def __init__(self, *args, **kwargs):
        super(PostProjectForm, self).__init__(*args,**kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Project Name...'
        self.fields['project_link'].widget.attrs['placeholder'] = 'Project Link...'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
