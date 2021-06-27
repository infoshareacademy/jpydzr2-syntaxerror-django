from django import forms
from django.contrib.auth.models import User
from account.models import Profile
from django.forms import PasswordInput


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Pass doesn\'t equal')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    married = forms.ChoiceField(choices=[(0 ,"No"), (1, "Yes")])
    education = forms.ChoiceField(choices=[(1, "Graduate"), (0, "Not Graduate")])
    class Meta:
        model = Profile
        fields = (
            'married', 'education', 'birth_date',
            'phone_num', 'street', 'str_building_no',
            'str_local_no', 'city', 'zip_code',
        )