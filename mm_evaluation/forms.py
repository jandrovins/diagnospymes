from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import django.forms as forms

from .models import PYME

class PYMERegistrationForm(forms.ModelForm):
    class Meta:
        model = PYME
        exclude = ('user')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
