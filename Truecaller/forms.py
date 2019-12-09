from django import forms
from Truecaller.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
class NewUserForm(UserCreationForm ):
    name = forms.CharField(max_length=100)
    mobile = forms.IntegerField()
    email = forms.EmailField(required=False)
    address = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ("name", "email")
        def save(self, commit=True):
            User = super(NewUserForm, self).save(commit=False)
            User.email = self.cleaned_data['email']
            if commit:
                User.save()
            return User


class UserSignUpForm(forms.Form):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("email", "password1","password2")
        def save(self, commit=True):
            User = super(UserSignUpForm, self).save(commit=False)
            email = self.cleaned_data['email'].strip()
            try:
                CustomUser.objects.get(email__iexact=email)
                raise forms.ValidationError('email already exists')
            except CustomUser.DoesNotExist:
                return email
            pw1 = self.cleaned_data.get('password1')
            pw2 = self.cleaned_data.get('password2')
            if pw1 and pw2 and pw1 == pw2:
                return pw2
            raise forms.ValidationError("passwords don't match")
            if commit:
                User.login()
            return User
