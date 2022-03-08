from django import forms
from users.models import User

class SignUpForm(forms.Form):

    username = forms.CharField(min_length= 4, max_length=15)
    email = forms.CharField(min_length=6,max_length=50,widget = forms.EmailInput())
    password = forms.CharField(max_length=70 , widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70 , widget=forms.PasswordInput())

    def clean_username(self):
        """Username must be unique"""

        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('El username ya existe')
        return username

    def clean(self):
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden')

        return data

    def save(self):
        data = self.cleaned_data
        data.pop('password_confirmation')

        user = User.objects.create_user(**data)
        user.save()