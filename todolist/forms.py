from django.forms import ModelForm
from .models import User, Service


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = ( 'title', 'time')