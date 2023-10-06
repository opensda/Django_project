from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from catalog.forms import StyleMixin
from users.models import User


class UserRegisterForm(StyleMixin, UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')



class UserForm(StyleMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password','first_name', 'last_name', 'phone', 'country',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


