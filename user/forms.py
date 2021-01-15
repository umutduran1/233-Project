from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    password = forms.CharField(max_length=100, label='Parola', widget=forms.PasswordInput())

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if username and password:

            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError("Kullanıcı adı veya parola hatalı!")

        return super(LoginForm, self).clean()


class RegisterForm(forms.ModelForm):
    
    first_name = forms.CharField(max_length=100,label='Ad')
    last_name = forms.CharField(max_length=100,label='Soyad')
    email = forms.EmailField(max_length=100,label='Email')
    password1 = forms.CharField(max_length=100, label='Parola',widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=100, label='Parola tekrar', widget=forms.PasswordInput())
    
    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def clean_password2(self):

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parolalar eşleşmiyor!")
        return password2





class UpdateProfileForm2(forms.ModelForm):

    class Meta:
        model = User

        fields = ['username','first_name','last_name']