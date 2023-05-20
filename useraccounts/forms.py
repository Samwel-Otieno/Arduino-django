from django.contrib.auth.models import User
from django import forms

class RegistrationForm(forms.ModelForm):
    password1=forms.CharField(label='password', widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    #model other parameters from the User method
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username','email']

    def validator(self):
        #the super method is valid only within a class it is used to call the validator method
        cleaned_data=super().validator()
        password1=self.cleaned_data.get("password1")
        password2=self.cleaned_data.get("password2")

        #validation 
        if (password1 == password2):
            raise forms.ValidationError("Passwords do not match")    
        return password1
    