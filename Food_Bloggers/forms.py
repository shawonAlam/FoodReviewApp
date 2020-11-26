from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class RegisterUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']
    
    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean_password2(self):
        cleaned_data = super().clean()
        pass1 = self.cleaned_data['password']
        pass2 = self.cleaned_data['password2']

        if pass1 != pass2:
            raise ValidationError('Password did not match')
        
        return pass2


